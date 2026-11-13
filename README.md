# Personal Finance

A personal finance transaction tracker built with Python and PostgreSQL.

## Features

- Add income and expense transactions.
- List registered transactions.
- Calculate total income and expenses.
- Check the current account balance.
- Update existing transactions.
- Delete transactions.
- Store transaction data in PostgreSQL.

## Technologies

- Python
- PostgreSQL
- Psycopg
- python-dotenv
- Git and GitHub

## Project Structure

```text
personal-finance/
├── .gitignore
├── .env
├── database.py
├── personal-finance.py
└── README.md
```

## Requirements

- Python 3
- PostgreSQL
- Git

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vitor-matheus2/personal-finance.git
```

2. Navigate to the project directory:

```bash
cd personal-finance
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install "psycopg[binary]" python-dotenv
```

## Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=personal_finance
DB_USER=postgres
DB_PASSWORD=your_password
```

Configure the PostgreSQL database and create the `transactions` table before running the application.

## Running the Project

```bash
python personal-finance.py
```

## Status

This project is under development and is part of my Python backend learning journey.
