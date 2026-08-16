# Overview

This Python script automates the process of reviewing and formatting Excel score data.

It reads data from an Excel workbook, checks the Score column, and identifies values greater than 50. Matching cells are automatically highlighted with a blue background and white text, making higher scores easy to identify at a glance.

The script uses Pandas to read and inspect Excel data and OpenPyXL to modify and format the workbook. The processed data is then saved as a new Excel file, leaving the original file unchanged.

# Business purpose

This automation reduces repetitive manual work involved in reviewing Excel reports, such as:

opening and reviewing spreadsheets
identifying scores that meet a specific threshold
manually highlighting important values
applying consistent formatting
saving the updated report


