import smtplib


def send_reminder():
    my_email = "valorantclipxs@gmail.com"
    password = "moiu uhuw pwur iuxi"

    ending_date = "21-JULY-2026"
    reminder_date = "7-JULY-2026"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="sandeepnegi5898@gmail.com",
            msg= f"subject: GEMINI PRO CANCELLATION REMENIDER\n\n Your Free subscription is ending on {ending_date}. Please cancel it on {reminder_date} to avoid charges. After {ending_date} monthly fees will be deducted."
        )

send_reminder()