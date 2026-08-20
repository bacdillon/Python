# Bagger Digital Preservation

Implementation using Streamlit, inspired by the supplied Bagger guide.<br>
This is NOT the official Library of Congress Bagger application. <br>
This demonstrates the **BagIt** digital preservation packaging standard, with libraries, archives, and institutions like the Library of Congress to package digital files for long-term storage and transfer, with built-in integrity verification.

## Overview

This project demonstrates how BagIt/Bagger packages, transfers, and validates digital files for preservation. The Rotterdam Deck Plans PDF is used as the sample payload. Users enter Bag Information, such as the bag name, transfer type, sender contact, and institution, then add the PDF. Bagger creates a BagIt package containing the file, metadata, and checksums. The bag can then be validated to confirm its structure and file integrity.
