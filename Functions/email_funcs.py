'''Functions for sending out emails with success/failure csv attachments'''

import smtplib, secrets
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def attach_file(msg, filepath):
    ''' Helper function for send_with_attachments: attach file to email

    param msg( MIMEMultipart): message Object
    param filepath(string): name of file to be attached
    '''
    attachment = open(filepath, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    attachment_name = filepath.split('/')[-1] if '/' in filepath else filepath
    part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_name)
    msg.attach(part)

def send_with_attachments(recipients, success_count=0, fail_count=0, success_file = None, fail_file= None, success=True, api_response = None):
    '''
    Sends email notification of results. Uses smtplib and email modules.

    param recipients (string): List of strings of email recipients
    params success_count, fail_count (integers): Number of successes/failures
    params success_file, fail_file (strings): New file names
    api_response (response object): Response object returned from Whispir API
    '''
    fromaddr = secrets.email
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = ", ".join(recipients)
    report = 'Success!' if success else 'Some issues:'
    msg['Subject'] = "Text Message Reminder Report: " + report

    if success:
        body = "Text message reminders have been sent out! Of the %s records in the spreadsheet, %s had valid data and %s did not. See attachments for details." %( success_count + fail_count, success_count, fail_count)
        if success_count: attach_file(msg, success_file)
        if fail_count: attach_file(msg, fail_file)
    else:
        body = "There was an issue with sending the data to the whisper API. The response message is below: \n \n "+    api_response.text

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(fromaddr, secrets.password)
    text = msg.as_string()
    server.sendmail(fromaddr, recipients, text)
    server.quit()
    print('email sent!')
