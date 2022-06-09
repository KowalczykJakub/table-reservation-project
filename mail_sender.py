import smtplib
from email.message import EmailMessage


def sendEmail(to: str, subject: str, content:str):
    s = smtplib.SMTP(host='smtp.ethereal.email', port=587)
    s.starttls()
    s.login('felipa.simonis91@ethereal.email', 'Bx3tz34GXqqPrk4QgV')

    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = subject
    msg['From'] = 'jacobos.plate@email.com'
    msg['To'] = to

    s.send_message(msg)
    s.quit()
    return 'Email sent!'