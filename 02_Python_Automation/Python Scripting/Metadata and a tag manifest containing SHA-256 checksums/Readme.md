# Overview

This Python script automates a daily sales reporting process from start to finish.

It takes multiple Excel sales files from an input folder, reads and validates the sales data, combines the information, calculates the total sales, and generates a standardized daily_sales_report.xlsx file.

It then creates supporting metadata and a tag manifest containing SHA-256 checksums, providing information about the report and helping verify file integrity.

Finally, when email credentials are configured, the script automatically sends the completed report and supporting files to the manager through Gmail.

# Business purpose

The automation replaces repetitive manual work such as:

- Collecting sales spreadsheets
- Copying and combining data
- Calculating totals
- Preparing reports
- Documenting the report
- Checking file integrity
- Sending reports by email

