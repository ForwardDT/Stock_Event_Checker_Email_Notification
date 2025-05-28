# Stock Event Checker & Email Notifications

A Python script that monitors upcoming earnings events for specified stocks, generates calendar invites (ICS files), and sends email reminders with the invite attached.

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [File Structure](#file-structure)
* [Utilities](#utilities)
* [Contributing](#contributing)
* [License](#license)

## Features

* Fetch upcoming earnings dates for a list of stock tickers using Yahoo Finance (`yfinance`).
* Generate `.ics` calendar invites for each earnings event.
* Send email notifications with the calendar invite attached.
* Configurable via environment variables.

## Prerequisites

* Python 3.7 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ForwardDT/Stock_Event_Checker_Email_Notification.git
   cd Stock_Event_Checker_Email_Notification
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root.
2. Define the following environment variables:

   ```ini
   SENDER_EMAIL_TOKEN=your_sender_email_address
   SENDER_PASSWORD_TOKEN=your_email_password_or_app_token
   RECIPIENT_EMAIL_TOKEN=recipient_email_address
   TICKERS=TSLA,GOOG,PLTR,RDDT   # comma-separated list of ticker symbols
   ```

## Usage

Run the main script to check earnings events and send notifications:

```bash
python main.py
```

* **Output**:

  * Calendar invite files are saved in the `ics_files/` directory (one `.ics` per ticker).
  * Email reminders with the invite attached are sent automatically to the recipient.

## File Structure

```
Stock_Event_Checker_Email_Notification/
├── main.py
├── requirements.txt
├── .env.example       # Example environment file (copy to .env)
├── ics_files/         # Generated calendar invites
└── utils/
    ├── calendar_utils.py  # Functions to create ICS content
    └── email_utils.py     # Functions to send email with attachment
```

## Utilities

* **calendar\_utils.create\_calendar\_event**: Builds an ICS event string given a ticker, date, and details.
* **email\_utils.send\_email\_with\_invite**: Sends an email with the provided ICS file attached.

