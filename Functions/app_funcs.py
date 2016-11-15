''' Miscelaneous application functions, that deal with higher level functionality (sending email, making API requests, etc)'''

import requests, secrets, smtplib, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from IPython import embed


def send_to_api(filename, encoded_csv):
    '''
    Sends data to Whispir API. Uses requests module.

    param filename (string): string of csv file oath
    param encoded_csv (bytes): csv file B64 encoded
    returns: HTTP response object
    '''

    url = "https://api.whispir.com/resources"
    querystring = {"apikey": secrets.key}

    payload = "{\"name\":\"%s\",\"scope\":\"private\",\"mimeType\":\"application/json\", \"derefUri\":\"%s\" }" %(filename, encoded_csv)

    # print(encoded_csv)
    headers = {

        'accept': "application/vnd.whispir.resource-v1+json",
        'content-type': "application/vnd.whispir.resource-v1+json"
        }

    response = requests.post( url, auth = (secrets.user, secrets.whispir_password), data=payload,
    headers=headers,
     params=querystring)
    # embed()
    # print(response.status_code, response.ok)
    print(response)
    return response


# ['dzgoldman@wesleyan.edu', 'dannyg9917@gmail.com']
def send_with_attachments(recipients, success_count=0, fail_count=0, success_file = None, fail_file= None, success=True, api_response = None):
    '''
    Sends email notification of results. Uses smtplib and email modultes.
    '''

    # Helper function for attaching a file
    def attach_file(msg, filename):
        attachment = open(filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

    fromaddr = secrets.email
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = ", ".join(recipients)
    report = 'Success!' if success else 'Some issues:'
    msg['Subject'] = "Text Message Reminder Report: " + report

    if success:
        body = "Text message reminders have been send out! Of the %s records in the spreadsheet, %s had valid data and %s did not. See attachments for details." %( success_count + fail_count, success_count, fail_count)
        if success_count: attach_file(msg, success_file)
        if fail_count: attach_file(msg, fail_file)
    else:
        body = "There was an issue with sending the data to the whisper API. The response message is below: \n \n "+    api_response.text


    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, secrets.password)
    text = msg.as_string()
    server.sendmail(fromaddr, recipients, text)
    server.quit()
