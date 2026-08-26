# Bagger Digital Preservation

Implementation using Streamlit, inspired by the supplied Bagger guide.
This is NOT the official Library of Congress Bagger application.
This demonstrates the BagIt digital preservation packaging standard, with libraries, archives, and institutions like the Library of Congress to package digital files for long-term storage and transfer, with built-in integrity verification.

## 1. Project Overview

This simple project demonstrates how BagIt/Bagger packages, transfers, and validates digital files for preservation. The Rotterdam Deck Plans PDF is used as the sample payload. Users enter Bag Information, such as the bag name, transfer type, sender contact, and institution, then add the PDF. Bagger creates a BagIt package containing the file, metadata, and checksums. The bag can then be validated to confirm its structure and file integrity.

## 2. Business Context

Archives, libraries, museums, and any organization responsible for long-term digital preservation records management departments, compliance and access teams, corporate archives and regularly need to package digital materials for transfer or storage in a way that can be verified later. If a file is corrupted, altered, or goes missing between when it's packaged and when it's opened years later, that's a serious problem for anyone relying on it as an authentic record. The BagIt standard exists specifically to solve this: it wraps files together with metadata and checksums so that integrity can always be checked, no matter how much time has passed.

## 3. Business Problem

Digital preservation and records transfer face a specific, recurring challenge:

- **Files can be altered or corrupted** during transfer, storage, or over long periods of time, with no way to detect it unless integrity information was captured up front.
- **There's often no standard way to package files with context** — who sent them, from what institution, for what purpose — alongside the files themselves.
- **Learning a formal preservation standard like BagIt is often abstract** without a hands-on tool to actually create and validate a Bag.
- **Verifying a package's integrity later requires the right structure and checksums to have been created correctly in the first place.**

## 4. Project Objectives

- Provide a simple, guided way to package files into a properly structured BagIt "Bag."
- Capture key sender and transfer metadata alongside the packaged files.
- Automatically generate checksums for every file, enabling integrity verification later.
- Allow any Bag to be validated, confirming its contents haven't been altered, added to, or removed.
- Serve as a practical, hands-on learning tool for the BagIt digital preservation standard.

## 5. What the Video Demonstrates

The video walks through the **"BagIt / Bagger Digital Preservation Learning App,"** covering both of its core functions:

- **Creating a Bag**: the user fills in bag information — a bag name ("rotterdam-deck-plans-2022"), type of transfer, sender email, sender contact, and sender institution ("Holland America Line") — then uploads a file (a PDF of historical ship deck plans) as the Bag's payload. Clicking **"Create Bag"** produces a properly structured Bag, shown as a directory containing the payload data folder alongside standard BagIt metadata files (`bag-info.txt`, `bagit.txt`, `manifest-md5.txt`, `tagmanifest-md5.txt`), including a visible MD5 checksum computed for the uploaded file. The completed Bag can then be downloaded as a ZIP file.
- **Validating a Bag**: the user uploads the just-created Bag ZIP file back into the app's validation tool and clicks **"Validate Bag."** The app checks the contents against their recorded checksums and reports **"PASS — all checked payload and tag files match their manifests,"** along with a summary confirming zero missing, extra, or modified files.

## 6. End-to-End Workflow, Step by Step

1. **Enter bag information.** The user provides a name for the Bag along with sender and transfer metadata (email, contact, institution, transfer type).
2. **Add the payload.** The user uploads one or more files to be preserved or transferred.
3. **Create the Bag.** The app packages the files into a standard BagIt structure, generating checksums for every file and recording the provided metadata.
4. **Review the Bag structure.** The app displays the resulting file structure and the payload manifest, showing the checksum recorded for each file.
5. **Download the Bag.** The completed Bag is available as a ZIP file for storage or transfer.
6. **Validate a Bag.** At any point, a Bag (freshly created or previously downloaded) can be uploaded back into the app for validation.
7. **Confirm integrity.** The app recalculates checksums for the Bag's contents and compares them against the recorded manifest, reporting a clear pass/fail result along with details of any missing, extra, or modified files.

## 7. Systems and Applications Involved

- **A Streamlit web application** — providing the Create Bag and Validate Bag interface
- **The BagIt specification** — the underlying digital preservation packaging standard being implemented and taught

## 8. Technologies Used

- **Python** — the language used to build the application
- **Streamlit** — for the web-based user interface
- **The BagIt packaging format** — including standard metadata files (`bagit.txt`, `bag-info.txt`) and manifest files
- **MD5 checksum generation** — for computing and verifying file integrity
- **ZIP file handling** — for packaging and unpackaging Bags for download and validation

## 9. Automation Logic

When a Bag is created, the app automates the parts of the BagIt standard that are easy to get wrong by hand: it organizes the uploaded files into the required `data` folder, generates the standard metadata files with the correct format, and computes a checksum for every payload file, recording all of them in a manifest. Validation reverses this process — it recalculates the checksum for every file currently in the Bag and compares it against what the manifest originally recorded, flagging any file that's missing, unexpectedly present, or has changed. This is what allows a Bag's integrity to be verified with confidence, long after it was originally created, without needing to trust that nothing happened to it in the meantime.

## 10. AI Capabilities

This project doesn't use AI. It is a direct, rules-based implementation of a formal preservation standard. Its value is in **correctly and consistently implementing a real specification**, which is exactly what a preservation standard requires: predictable, verifiable behavior, not judgment or interpretation.

## 11. User Interactions

- Users fill in a straightforward form to provide Bag and sender information.
- Users upload files through a simple drag-and-drop or browse interface.
- A single button click creates a fully structured, checksum-verified Bag.
- Validating a Bag is equally simple — upload the Bag ZIP (or use the one just created) and click to validate, receiving a clear pass/fail result.

## 12. Inputs and Outputs

**Inputs:**
- Bag metadata: bag name, type of transfer, sender email, sender contact, sender institution
- One or more files to be packaged as the Bag's payload
- For validation: a previously created Bag (as a ZIP file)

**Outputs:**
- A properly structured BagIt package, including metadata files and a payload manifest with checksums
- A downloadable ZIP file containing the complete Bag
- A validation report confirming whether a Bag's contents match its recorded manifest, including counts of any missing, extra, or modified files

## 13. Error Handling and Validation

- The entire **purpose** of the Validate Bag function is error detection: it exists specifically to catch missing files, unexpected additional files, or files that have been altered since the Bag was created.
- Checksums are generated automatically at creation time, removing the risk of a manually calculated or recorded checksum being wrong.
- The validation report is explicit and quantified (0 missing, 0 extra, 0 modified in the demonstrated example), rather than a vague pass/fail with no detail.

## 14. Business Rules

- A Bag must include the standard BagIt metadata files (`bagit.txt`, `bag-info.txt`) alongside its payload.
- Every payload file must have a corresponding checksum recorded in the manifest at creation time.
- Validating a Bag must check every file against its recorded checksum and clearly report any discrepancy.
- A Bag is only considered valid if all checked payload and tag files match their manifests exactly.

## 15. Key Features Demonstrated

- Guided creation of a standards-compliant BagIt package
- Automatic checksum generation for payload integrity
- Clear visualization of the resulting Bag structure and manifest
- Downloadable, portable Bag packages (ZIP format)
- Independent validation of any Bag, confirming its integrity
- An accessible, hands-on way to learn a formal digital preservation standard

## 16. Business Value and Benefits

- **Protects the integrity of digital records** over time, by capturing verifiable checksums at the point of packaging.
- **Standardizes how files are packaged for transfer or archiving**, rather than relying on ad hoc folder structures.
- **Builds practical skills** in a real, industry-recognized preservation standard, in a safe, hands-on environment.
- **Provides confidence during transfers** — a recipient can independently validate that what they received matches what was sent.
- **Supports compliance and audit needs** in records management, where provable data integrity may be a formal requirement.

## 17. Productivity Improvements

- Removes the need to manually create BagIt-compliant folder structures and metadata files by hand.
- Automates checksum generation, which would otherwise require separate tools or manual calculation.
- Makes Bag validation a one-click process rather than a manual, file-by-file comparison.

## 18. Real-World Enterprise Use Cases

The BagIt pattern, and this kind of learning tool, applies directly to:

- **Library and archive digital collections management** — packaging digitized materials for long-term storage
- **Institutional records transfer** — moving records between departments or organizations with verifiable integrity
- **Corporate compliance archiving** — preserving records in a way that can prove they haven't been altered
- **Digital preservation training programs** — teaching archivists and records managers a real, applicable standard
- **Any regulated data transfer scenario** — where proving a file hasn't changed since a specific point in time matters

## 19. Lessons Learned

- Implementing a real, external standard (rather than inventing an ad hoc format) means the resulting packages are portable and recognizable to anyone else familiar with BagIt.
- Automating checksum generation at the point of creation is what makes later verification meaningful — integrity checking is only as good as the original record it's compared against.
- A clear, quantified validation result (missing/extra/modified counts) is far more useful than a simple pass/fail, especially when troubleshooting a failed validation.
- Building a hands-on tool is often the most effective way to teach a formal standard — using BagIt directly makes the specification concrete in a way reading about it doesn't.
- Clearly labeling an educational tool as distinct from the official application it's inspired by is good practice, avoiding any confusion about authority or certification.

## 20. Possible Future Enhancements

- Support additional checksum algorithms (such as SHA-256) alongside MD5, matching modern preservation best practices.
- Add support for packaging multiple files or entire folder structures as a single Bag payload.
- Include a guided walkthrough or tooltip explanations of each part of the BagIt standard for newer learners.
- Add batch validation, checking multiple Bags at once.
- Provide a detailed, downloadable validation report for record-keeping purposes.
- Add integration with cloud or institutional storage systems for direct Bag upload and retrieval.
