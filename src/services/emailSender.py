from typing import List, Optional, cast
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os


class EmailSender():
    username = ""
    password = ""
    port = 587
    host = ""
    mailAddress = ""

    def __init__(self, mailAddress, username, password, host):
        self.mailAddress = mailAddress
        self.username = username
        self.password = password
        self.host = host

    def sendEmail(self, address_book: List[str], subject: str, html: str, attachmentFpath: Optional[str] = None) -> None:
        """send mail to recepients
        Args:
            address_book (List[str]): list of target mail addresses
            subject (str): mail subject 
            html (str): mail body
            attachmentFpath (str): file path of attachment file
        """
        msg = MIMEMultipart()
        msg['From'] = self.mailAddress
        msg['To'] = ','.join(address_book)
        msg['Subject'] = subject
        # msg.attach(MIMEText(body, 'plain'))
        msg.attach(MIMEText(html, 'html'))
        
        if not(attachmentFpath == None) and not(attachmentFpath == ""):
            fPath = cast(str, attachmentFpath)
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(fPath, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="{0}"'.format(os.path.basename(fPath)))
            msg.attach(part)
        
        text = msg.as_string()
        # Send the message via our SMTP server
        s = smtplib.SMTP(self.host, self.port)
        s.starttls()
        s.login(self.username, self.password)
        s.sendmail(self.mailAddress, address_book, text)
        s.quit()
