''' Miscelaneous application functions, that deal with higher level functionality (sending email, making API requests, etc)'''

import requests, secrets, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_to_api(filename, encoded_csv):
    '''
    Sends data to Whispir API. Uses requests module

    param filename (string): string of csv file oath
    param encoded_csv (bytes): csv file B64 encoded
    returns: HTTP response object
    '''

    url = "https://api.whispir.com/resource"
    querystring = {"apikey": secrets.key}

    payload ={
        'name': filename,
         "scope" : "private",
         "mimeType" : "application/json",
         "derefUri" : encoded_csv
    }
    headers = {

        'authorization': secrets.auth,
        # 'accept': "application/vnd.whispir.resource-v1+json",
        'content-type': "application/vnd.whispir.resource-v1+json"
        }

    response = requests.post( url, auth = (secrets.user, secrets.whispir_password), data=payload,
    # headers=headers,
     params=querystring)

    print(response.text)


# ['dzgoldman@wesleyan.edu', 'dannyg9917@gmail.com']
def send_with_attachments(recipients, path, success_count, fail_count):
    '''
    Sends mass email notification with csv of succesfully contacted records as attachment. Users smtplib and email modules

    param recipients(list): strings of email addresses
    param path (str): path of csv file to be attached
    param success_count (int): number of messages successfully sent out
    param fail_count (int): number of messages that failed to send
    returns: None
    '''

    fromaddr = secrets.email
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = "SUBJECT OF THE EMAIL"

    body = "Blah blah"

    msg.attach(MIMEText(body, 'plain'))

    filename = "successes.csv"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, secrets.password)
    text = msg.as_string()
    server.sendmail(fromaddr, recipients, text)
    server.quit()
