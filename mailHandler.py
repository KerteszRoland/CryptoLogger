import smtplib
import txtHandler

EMAIL_ADDRESS = txtHandler.GetFromEmailAddress()
PASSWORD = txtHandler.GetEmailPassword()
SMTP_EMAIl = txtHandler.GetSMTPEmail()


def SendEmail(email_to, title, text):
    print("Logging in...")
    with smtplib.SMTP(SMTP_EMAIl, 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, PASSWORD)
        msg = f'Subject: {title}\n\n{text}'
        smtp.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=email_to, msg=msg)
    print("Email sent!")
