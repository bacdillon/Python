# 30 Unique Python Scripts for `dbo.airbnb_listings`

These scripts are based on the visible SQL Server table structure:

- `id` — primary key, int, not null
- `city` — varchar(50), nullable
- `country` — varchar(50), nullable
- `number_of_rooms` — int, nullable
- `year_listed` — int, nullable

## Setup

Install the SQL Server ODBC driver and Python package:

```bash
pip install pyodbc
```

Set these environment variables before running a script:

- `DB_SERVER`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_DRIVER` (optional; defaults to `ODBC Driver 17 for SQL Server`)

Example:

```bash
python 08_count_by_country.py
```

Scripts 03, 04, 05, 06, and 25 ask for a value interactively.
