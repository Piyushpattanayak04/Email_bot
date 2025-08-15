📧 Bulk Email Sender






A simple yet powerful bulk email sender script built in Python to send personalized Hack O'Clock guidelines to all participants from a CSV file.

🚀 Features

✅ Personalized Emails – Each participant gets a customized message with their details.
✅ Secure Sending – Uses Gmail SMTP over SSL.
✅ Tracking – Logs sent emails to devFolioDone.csv.
✅ Lightweight – No external dependencies, just Python’s standard library.

📂 How It Works

Reads participant details from test.csv:

MemberName,Email,TeamName,SecurityCode
John Doe,john@example.com,CodeMasters,ABC123


Generates a personalized guidelines email.

Sends via Gmail SMTP.

Records the sent entry in devFolioDone.csv for reference.

📦 Requirements

Python 3.x

A Gmail account with an App Password enabled.

🔧 Setup & Usage

Clone this repository

git clone https://github.com/yourusername/piyushpattanayak04-email_bot.git
cd piyushpattanayak04-email_bot


Prepare your CSV file (test.csv):

MemberName,Email,TeamName,SecurityCode
Alice Smith,alice@example.com,Innovators,XYZ789


Configure Gmail credentials in app.py:

sender = "youremail@gmail.com"
password = "your_app_password"


Run the script:

python app.py

⚠️ Important Notes

Never commit your real Gmail credentials to GitHub. Use .gitignore to hide sensitive files.

Gmail has sending limits (~500/day for regular accounts).

Always use App Passwords instead of your main Gmail password for security.
