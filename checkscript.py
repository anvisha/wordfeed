import smtplib

def send_email(text):
    SERVER = "localhost"

    FROM = "anvisha@gmail.com"
    TO = ["anvisha@gmail.com"] # must be a list

    SUBJECT = "Hello!"

    TEXT = "This message was sent with Python's smtplib."

    # Prepare actual message

    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail

    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()
