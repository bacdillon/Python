import io
import hashlib
import zipfile
from datetime import datetime, timezone
from pathlib import PurePosixPath
import streamlit as st

st.set_page_config(page_title="Python BagIt Bagger", page_icon="📦", layout="wide")
st.title("📦 Bagger Digital Preservation")
st.write("**Educational Streamlit implementation inspired by the supplied Bagger guide.**")
st.warning("This is NOT the official Library of Congress Bagger application.")

def md5_bytes(data):
    return hashlib.md5(data).hexdigest()

def create_bag(files, bag_name, email, contact, institution, transfer, address):
    out = io.BytesIO()
    entries = []
    tags = {}

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            data = f.getvalue()
            name = PurePosixPath(f.name).name
            z.writestr(f"{bag_name}/data/{name}", data)
            entries.append(f"{md5_bytes(data)}  data/{name}")

        bag_it = "BagIt-Version: 0.97\nTag-File-Character-Encoding: UTF-8\n"
        z.writestr(f"{bag_name}/bag-it.txt", bag_it)
        tags["bag-it.txt"] = bag_it.encode()

        lines = [
            f"Sender-Email: {email}",
            f"Sender-Contact: {contact}",
            f"Sender-Institution: {institution}",
            f"Type-Of-Transfer: {transfer}",
        ]
        if address.strip():
            lines.append(f"Sender-Address: {address}")
        lines.append("Bagging-Date: " + datetime.now(timezone.utc).isoformat())
        bag_info = "\n".join(lines) + "\n"
        z.writestr(f"{bag_name}/bag-info.txt", bag_info)
        tags["bag-info.txt"] = bag_info.encode()

        manifest = "\n".join(entries) + "\n"
        z.writestr(f"{bag_name}/manifest-md5.txt", manifest)
        tags["manifest-md5.txt"] = manifest.encode()

        tag_manifest = "\n".join(
            f"{md5_bytes(data)}  {name}" for name, data in tags.items()
        ) + "\n"
        z.writestr(f"{bag_name}/tagmanifest-md5.txt", tag_manifest)

    return out.getvalue(), entries

def validate_bag(zip_bytes):
    result = {"missing": [], "extra": [], "modified": [], "tag_missing": [], "tag_modified": []}
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
        names = z.namelist()
        tops = {n.split("/")[0] for n in names if "/" in n}
        if len(tops) != 1:
            raise ValueError("ZIP must contain one top-level bag directory.")
        bag = next(iter(tops))
        prefix = bag + "/"

        manifest_name = prefix + "manifest-md5.txt"
        if manifest_name not in names:
            raise ValueError("manifest-md5.txt is missing.")

        expected = {}
        for line in z.read(manifest_name).decode().splitlines():
            if line.strip():
                checksum, path = line.split(maxsplit=1)
                expected[path] = checksum

        actual = {}
        data_prefix = prefix + "data/"
        for name in names:
            if name.startswith(data_prefix) and not name.endswith("/"):
                relative = name[len(prefix):]
                actual[relative] = md5_bytes(z.read(name))

        result["missing"] = sorted(set(expected) - set(actual))
        result["extra"] = sorted(set(actual) - set(expected))
        result["modified"] = sorted(
            p for p in set(expected) & set(actual) if expected[p] != actual[p]
        )

        tag_name = prefix + "tagmanifest-md5.txt"
        if tag_name in names:
            expected_tags = {}
            for line in z.read(tag_name).decode().splitlines():
                if line.strip():
                    checksum, filename = line.split(maxsplit=1)
                    expected_tags[filename] = checksum
            for filename, checksum in expected_tags.items():
                full = prefix + filename
                if full not in names:
                    result["tag_missing"].append(filename)
                elif md5_bytes(z.read(full)) != checksum:
                    result["tag_modified"].append(filename)
    return result

create_tab, validate_tab, about_tab = st.tabs(["👜 Create Bag", "✅ Validate Bag", "ℹ️ About"])

with create_tab:
    st.subheader("1. Bag Information")
    c1, c2 = st.columns(2)
    with c1:
        bag_name = st.text_input("Bag name", "example_bag_2026_08")
        email = st.text_input("Sender Email", "archivist@example.org")
        contact = st.text_input("Sender Contact", "Example Contact")
        institution = st.text_input("Sender Institution", "Example Organisation")
    with c2:
        transfer = st.selectbox("Type of Transfer", ["Network", "Hard Drive", "CD/DVD"])
        address = st.text_area("Sender Address (optional)")
    st.subheader("2. Payload")
    files = st.file_uploader("Add files to the payload", accept_multiple_files=True)

    if files:
        st.write(f"**{len(files)} file(s) selected.**")
        for f in files:
            st.write(f"- `{f.name}` ({f.size:,} bytes)")

    if st.button("📦 Create Bag", type="primary", disabled=not files):
        if not bag_name.strip():
            st.error("Please enter a bag name.")
        else:
            data, entries = create_bag(files, bag_name.strip(), email, contact, institution, transfer, address)
            st.session_state["latest_bag"] = data
            st.success("Bag created successfully.")
            st.code(f"""{bag_name}/
├── data/
├── bag-info.txt
├── bag-it.txt
├── manifest-md5.txt
└── tagmanifest-md5.txt
""")
            st.write("### Payload Manifest")
            st.code("\n".join(entries))
            st.download_button("⬇️ Download Bag as ZIP", data, f"{bag_name}.zip", "application/zip")

with validate_tab:
    st.subheader("Validate a BagIt ZIP")
    source = st.radio("Choose validation source", ["Latest bag created in this session", "Upload a Bag ZIP"])
    data = st.session_state.get("latest_bag") if source.startswith("Latest") else None
    if source.startswith("Upload"):
        uploaded = st.file_uploader("Upload Bag ZIP", type=["zip"], key="validation_zip")
        if uploaded:
            data = uploaded.getvalue()

    if st.button("🔍 Validate Bag", type="primary", disabled=data is None):
        try:
            r = validate_bag(data)
            if not any(r.values()):
                st.success("PASS — all checked payload and tag files match their manifests.")
            else:
                st.error("FAIL — one or more validation checks require investigation.")
            a, b, c = st.columns(3)
            a.metric("Missing", len(r["missing"]))
            b.metric("Extra", len(r["extra"]))
            c.metric("Modified", len(r["modified"]))
            for key, title in [
                ("missing", "Missing payload files"),
                ("extra", "Unexpected payload files"),
                ("modified", "Modified payload files"),
                ("tag_missing", "Missing tag files"),
                ("tag_modified", "Modified tag files"),
            ]:
                if r[key]:
                    st.write(f"### {title}")
                    for item in r[key]:
                        st.write(f"- `{item}`")
        except Exception as e:
            st.error(f"Validation error: {e}")

with about_tab:
    st.subheader("How this maps to Bagger")
    st.markdown("""
| Bagger concept | Streamlit implementation |
|---|---|
| Create New Bag | Create Bag button |
| Bag-Info | Sender metadata form |
| Payload | Uploaded files |
| `data/` | Payload directory |
| `bag-it.txt` | Generated automatically |
| `manifest-md5.txt` | Payload checksums |
| `tagmanifest-md5.txt` | Tag-file checksums |
| Validation | Validate Bag tab |
| Missing files | Detected |
| Added/extra files | Detected |
| Modified files | Detected by checksum mismatch |
| ZIP serialization | Downloaded ZIP |
""")
    st.info("Use this as a learning/portfolio implementation. It is not the official Library of Congress Bagger software.")
