import datetime
import yfinance as yf
import os
from dotenv import load_dotenv

from utils.calendar_utils import create_calendar_event
from utils.email_utils import send_email_with_invite

# Load variables from .env into the environment
load_dotenv()

sender_email_token = os.environ.get("SENDER_EMAIL_TOKEN")
sender_password_token = os.environ.get("SENDER_PASSWORD_TOKEN")
recipient_email_token = os.environ.get("RECIPIENT_EMAIL_TOKEN")

# tickers_str = os.environ.get("TICKERS", "")
# tickers = [ticker.strip() for ticker in tickers_str.split(",") if ticker.strip()]
tickers = ['RDDT', 'TSLA', 'GOOG', 'PLTR']


# Define a dedicated folder for ICS files
ics_folder = "ics_files"
os.makedirs(ics_folder, exist_ok=True)

if __name__ == "__main__":
    today = datetime.date.today()

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        try:
            calendar = stock.calendar
            if calendar is not None and 'Earnings Date' in calendar:
                earnings_date_value = calendar['Earnings Date'][0]
                if isinstance(earnings_date_value, datetime.date):
                    earnings_date = earnings_date_value
                else:
                    earnings_date = datetime.datetime.strptime(str(earnings_date_value), "%Y-%m-%d").date()
                    
                days_left = (earnings_date - today).days

                earnings_high    = calendar.get('Earnings High', 'N/A')
                earnings_low     = calendar.get('Earnings Low', 'N/A')
                earnings_avg     = calendar.get('Earnings Average', 'N/A')
                revenue_high     = calendar.get('Revenue High', 'N/A')
                revenue_low      = calendar.get('Revenue Low', 'N/A')
                revenue_avg      = calendar.get('Revenue Average', 'N/A')

                details = (
                    f"{ticker} earnings report scheduled on {earnings_date}. Days left: {days_left}\n"
                    f"Earnings High: {earnings_high}\n"
                    f"Earnings Low: {earnings_low}\n"
                    f"Earnings Average: {earnings_avg}\n"
                    f"Revenue High: {revenue_high}\n"
                    f"Revenue Low: {revenue_low}\n"
                    f"Revenue Average: {revenue_avg}"
                )

                ics_content = create_calendar_event(ticker, earnings_date, details)
                ics_filename = f"{ticker}_event.ics"
                filepath = os.path.join(ics_folder, ics_filename)
                
                with open(filepath, "w") as f:
                    f.write(ics_content)

                subject = f"Stock Event: {ticker} Earnings Report Reminder"
                body = (
                    f"Dear Investor,\n\n"
                    f"Reminder: {ticker} has an earnings report on {earnings_date}.\n\n"
                    f"Details:\n{details}\n\n"
                    f"The calendar invite is attached for your convenience.\n\n"
                    f"Best regards."
                )

                send_email_with_invite(
                    sender_email_token,
                    sender_password_token,
                    recipient_email_token,
                    subject,
                    body,
                    filepath  # now pointing to the file inside the dedicated folder
                )
            else:
                print(f"No earnings event found for {ticker}.")
        except Exception as e:
            print(f"Error retrieving data for {ticker}: {e}")