# 📧 Reminder Automation Mail

I have Created this python script so that I get a monthly reminder about my GEMINI PRO free subscription. so that i could cancel it before the Time period.

## 🚀 Features

- Sends automated email reminders
- Configurable date (e.g., send 1 week before the subscription ends)
- Used Gmail SMTP for email delivery
- Can be scheduled to run automatically (e.g., daily or monthly)
- Hosted on Pythonanywhere cloud.

## 🛠️ Technologies Used

- Python 3.x
- `smtplib` for sending emails
- `datetime` for scheduling logic
- PythonAnywhere for automated cloud execution

## 🧠 How It Works

1. The script checks if the current date is the predefined reminder date (e.g., 14th of the month).
2. If it matches, it sends an email using your Gmail credentials via SMTP.
3. Can be deployed on PythonAnywhere with daily scheduled tasks.

## 📂 Project Structure

```bash
Reminder-automation-mail/
├── main.py        # Core script that checks date & sends email
├── README.md      # Project documentation
├── requirements.txt (optional)
└── venv/          # Python virtual environment (not uploaded to GitHub)
```
## ⚙️ Setup Instructions

Follow these steps to run the project locally or on a cloud platform like PythonAnywhere.

### 1. Clone the repository

```bash
git clone https://github.com/SANDEEPNEGI07/Reminder-automation-mail.git
cd Reminder-automation-mail
```

### You can copy paste my code, Change the sender and reciever email and your password (which you can create on gmail under App Password section).
