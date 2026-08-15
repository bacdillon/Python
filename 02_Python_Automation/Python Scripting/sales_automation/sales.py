from pathlib import Path
import hashlib
import os
import pandas as pd
import smtplib

from email.message import EmailMessage


# ============================================================
# 1. CONFIGURATION
# ============================================================

# Folder containing the source Excel files
INPUT_FOLDER = Path("input")

# Folder where all generated files will be saved
OUTPUT_FOLDER = Path("output")

# Name of the completed sales report
REPORT_FILE = OUTPUT_FOLDER / "daily_sales_report.xlsx"

# Name of the metadata file
METADATA_FILE = OUTPUT_FOLDER / "daily_sales_report_metadata.txt"

# Name of the tag manifest
MANIFEST_FILE = OUTPUT_FOLDER / "tag_manifest.txt"


# ============================================================
# 2. EMAIL CONFIGURATION
# ============================================================

# Get email credentials from environment variables.
# This is safer than putting your password directly
# inside the Python script.

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_APP_PASSWORD")

MANAGER_EMAIL = os.getenv("MANAGER_EMAIL")


# ============================================================
# 3. CREATE OUTPUT FOLDER
# ============================================================

# Create the output folder if it doesn't already exist.
OUTPUT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 4. FIND EXCEL FILES
# ============================================================

# Find every .xlsx file inside the input folder.
excel_files = list(INPUT_FOLDER.glob("*.xlsx"))


# Stop the program if no Excel files were found.
if not excel_files:
    raise FileNotFoundError(
        "No Excel files were found in the input folder."
    )


print(f"Found {len(excel_files)} Excel files.")


# ============================================================
# 5. READ SALES DATA
# ============================================================

# This list will contain the data from every Excel file.
all_data = []


# Process each Excel file individually.
for file in excel_files:

    print(f"Processing: {file.name}")

    # Read the Excel file into a Pandas DataFrame.
    df = pd.read_excel(file)

    # Check that the required Sales column exists.
    if "Sales" not in df.columns:

        print(
            f"Skipping {file.name}: "
            "'Sales' column was not found."
        )

        continue

    # Add the original filename to the data.
    # This helps identify where each record came from.
    df["Source File"] = file.name

    # Add this DataFrame to our collection.
    all_data.append(df)


# ============================================================
# 6. VALIDATE DATA
# ============================================================

# Stop if none of the files contained valid sales data.
if not all_data:
    raise ValueError(
        "No valid sales data was found."
    )


# ============================================================
# 7. COMBINE ALL SALES DATA
# ============================================================

# Combine all DataFrames into one table.
combined_data = pd.concat(
    all_data,
    ignore_index=True
)


# ============================================================
# 8. CALCULATE TOTAL SALES
# ============================================================

# Add together every value in the Sales column.
total_sales = combined_data["Sales"].sum()

print(f"Total sales: ${total_sales:,.2f}")


# ============================================================
# 9. CREATE SUMMARY
# ============================================================

# Create a small summary table for the report.
summary = pd.DataFrame({
    "Metric": [
        "Number of source files",
        "Number of sales records",
        "Total sales"
    ],

    "Value": [
        len(excel_files),
        len(combined_data),
        total_sales
    ]
})


# ============================================================
# 10. CREATE EXCEL REPORT
# ============================================================

# Create the Excel workbook.
with pd.ExcelWriter(
    REPORT_FILE,
    engine="openpyxl"
) as writer:

    # Write the summary to the Summary worksheet.
    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    # Write all sales records to the Sales Data worksheet.
    combined_data.to_excel(
        writer,
        sheet_name="Sales Data",
        index=False
    )


print(
    f"Report created: {REPORT_FILE}"
)


# ============================================================
# 11. CALCULATE SHA-256 CHECKSUM
# ============================================================

def calculate_checksum(filename):
    """
    Calculate the SHA-256 checksum of a file.
    """

    sha256 = hashlib.sha256()

    # Open the file in binary read mode.
    with open(filename, "rb") as file:

        # Read the file in 4 KB chunks.
        for data in iter(
            lambda: file.read(4096),
            b""
        ):

            # Add each chunk to the checksum calculation.
            sha256.update(data)

    # Return the final SHA-256 hash.
    return sha256.hexdigest()


# Calculate the checksum of the completed Excel report.
report_checksum = calculate_checksum(
    REPORT_FILE
)


# ============================================================
# 12. CREATE METADATA FILE
# ============================================================

metadata = f"""
DAILY SALES REPORT METADATA
===========================

File Name:
{REPORT_FILE.name}

File Type:
Microsoft Excel Workbook (.xlsx)

Report Type:
Daily Sales Report

Generated By:
Python Sales Automation

Generation Date:
14 August 2026

Source Files:
{chr(10).join("  - " + file.name for file in excel_files)}

Source File Count:
{len(excel_files)}

Sales Record Count:
{len(combined_data)}

Total Sales:
${total_sales:,.2f}

Currency:
USD

Workbook Sheets:
  - Summary
  - Sales Data

Processing:
  - Located Excel source files
  - Read sales data using Pandas
  - Validated the Sales column
  - Combined source data
  - Calculated total sales
  - Generated consolidated Excel report

Automation Status:
Completed

Report Status:
Final

Integrity:
Checksum Algorithm: SHA-256
SHA-256:
{report_checksum}

Associated Tag Manifest:
tag_manifest.txt
"""


# Save the metadata to a text file.
METADATA_FILE.write_text(
    metadata.strip(),
    encoding="utf-8"
)


print(
    f"Metadata created: {METADATA_FILE}"
)


# ============================================================
# 13. CREATE TAG MANIFEST
# ============================================================

# Calculate the checksum of the metadata file.
metadata_checksum = calculate_checksum(
    METADATA_FILE
)


# Create the manifest.
manifest = f"""
TAG MANIFEST
============

Report File:
{REPORT_FILE.name}

SHA-256:
{report_checksum}


Metadata File:
{METADATA_FILE.name}

SHA-256:
{metadata_checksum}
"""


# Save the manifest.
MANIFEST_FILE.write_text(
    manifest.strip(),
    encoding="utf-8"
)


print(
    f"Tag manifest created: {MANIFEST_FILE}"
)


# ============================================================
# 14. EMAIL THE REPORT
# ============================================================

# Only attempt to send the email if ALL required
# credentials have been configured.
#
# The original version checked for specific hard-coded
# email addresses and an EMPTY password.
#
# This version simply checks whether the environment
# variables contain values.
if (
    SENDER_EMAIL
    and SENDER_PASSWORD
    and MANAGER_EMAIL
):

    # Create a new email.
    message = EmailMessage()

    # Set the email subject.
    message["Subject"] = "Daily Sales Report"

    # Set the sender.
    message["From"] = SENDER_EMAIL

    # Set the recipient.
    message["To"] = MANAGER_EMAIL

    # Create the email body.
    message.set_content(
        f"""
Hello,

The daily sales report has been generated automatically.

Source files processed: {len(excel_files)}
Sales records: {len(combined_data)}
Total sales: ${total_sales:,.2f}

The completed report is attached.

SHA-256:
{report_checksum}

Regards,
Sales Automation
"""
    )


    # ========================================================
    # 15. ATTACH THE EXCEL REPORT
    # ========================================================

    # Open the Excel report as binary data.
    with open(REPORT_FILE, "rb") as file:

        # Add the Excel report as an attachment.
        message.add_attachment(
            file.read(),

            maintype="application",

            subtype=(
                "vnd.openxmlformats-officedocument."
                "spreadsheetml.sheet"
            ),

            filename=REPORT_FILE.name
        )


    # ========================================================
    # 16. ATTACH THE METADATA
    # ========================================================

    # Open the metadata file.
    with open(METADATA_FILE, "rb") as file:

        # Add the metadata as an attachment.
        message.add_attachment(
            file.read(),
            maintype="text",
            subtype="plain",
            filename=METADATA_FILE.name
        )


    # ========================================================
    # 17. ATTACH THE TAG MANIFEST
    # ========================================================

    # Open the manifest file.
    with open(MANIFEST_FILE, "rb") as file:

        # Add the manifest as an attachment.
        message.add_attachment(
            file.read(),
            maintype="text",
            subtype="plain",
            filename=MANIFEST_FILE.name
        )


    # ========================================================
    # 18. CONNECT TO GMAIL
    # ========================================================

    try:

        # Connect securely to Gmail's SMTP server.
        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            # Log into the Gmail account using
            # the Google App Password.
            smtp.login(
                SENDER_EMAIL,
                SENDER_PASSWORD
            )

            # Send the completed email.
            smtp.send_message(message)


        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:

        # Gmail rejected the login.
        print(
            "Email authentication failed."
        )

        print(
            "Make sure SENDER_APP_PASSWORD contains "
            "a valid Google App Password."
        )

    except Exception as error:

        # Handle other email errors.
        print(
            f"Email could not be sent: {error}"
        )


else:

    # Don't send email if credentials haven't been configured.
    print(
        "Email was not sent because "
        "email credentials are not configured."
    )


# ============================================================
# 19. FINAL STATUS
# ============================================================

print()
print("======================================")
print("SALES AUTOMATION COMPLETED")
print("======================================")
print(f"Report:   {REPORT_FILE}")
print(f"Metadata: {METADATA_FILE}")
print(f"Manifest: {MANIFEST_FILE}")
print(f"Total:    ${total_sales:,.2f}")
print(f"SHA-256:  {report_checksum}")
print("======================================")