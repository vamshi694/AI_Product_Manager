from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import smtplib
import os

load_dotenv(".env")

def send_email(subject = "", body = "", attachments = None):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg.attach(MIMEText(body))

    if attachments is not None: 
        if type(attachments) is not list: 
            attachments = [attachments]   

        for each_attachment in attachments:        
            with open(each_attachment, 'rb') as f: 
                file = MIMEApplication( 
                    f.read(), 
                    name = os.path.basename(each_attachment) 
                ) 
            file["Content-Disposition"] = f'''attachment; filename = "{os.path.basename(each_attachment)}"''' 
            msg.attach(file)

        smtp = smtplib.SMTP("smtp.gmail.com", 587) 
        smtp.ehlo() 
        smtp.starttls() 
        smtp.login(os.getenv("APP_MAIL_ID"), os.getenv("APP_PASSCODE"))

        smtp.sendmail(os.getenv("FROM_ADD"), 
                to_addrs = os.getenv("TO_ADD"), msg = msg.as_string()) 

        smtp.quit()

    return "An email is sent to you with a summary of this meeting.\nThank you!!"