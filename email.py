  # -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:07:24 2020

@author: Heeje Cho

Module contains class BioceptEmailer to send out automated emails to reciepients
Class: Emailer
"""

import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


class Emailer:
    def __init__(self, email, password, subject, recipients):
        self.server = 'smtp-mail.outlook.com'
        self.subject = subject
        self.recipients = recipients
        self.htmlbody = ''
        self.email = email
        self.password = password
        self.attachments = []

    def send(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.email
        msg['Subject'] = self.subject
        msg['To'] = ", ".join(self.recipients)
        msg.preamble = "Preamble goes here"
        #check if there are attachments, if yes then add
        if self.attachments:
            self.attach(msg)
        #add htmlbody after attachments
        msg.attach(MIMEText(self.htmlbody, 'html'))
        #send
        s = smtplib.SMTP(self.server)
        s.connect(self.server)
        s.ehlo()
        s.starttls()
        s.login(self.email, self.password)
        s.sendmail(self.email, self.recipients, msg.as_string())

        s.quit()

    def htmladd(self, html):
        self.htmlbody = self.htmlbody+'<p></p>'+html

    def attach(self, msg):
        for f in self.attachments:
            if os.path.isabs(f) == True:
                fname = os.path.basename(f)
            else:
                fname = f

            ctype, encoding = mimetypes.guess_type(f)
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"

            maintype, subtype = ctype.split('/',1)

            if maintype == 'text':
                fp = open(f)
                #Note: we should handle calculating the charset
                attachment = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'image':
                fp = open(f, 'rb')
                attachment = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'audio':
                fp = open(f, 'rb')
                attachment = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(f, 'rb')
                attachment = MIMEBase(maintype, subtype)
                attachment.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', 'attachment', filename=fname)
            attachment.add_header('Content-ID', '<{}>'.format(fname))
            msg.attach(attachment)

    def addattach(self, files):
        self.attachments = self.attachments + files

