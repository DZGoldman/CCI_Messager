
import requests,   secrets


def send_to_api(encoded_csv):
    url = "https://api.whispir.com/resource"

    querystring = {"apikey":"yzxwb8pukthnsjyjfnqw9hew"}

    payload ={
        'name': '<filename>',
         "scope" : "private",
         "mimeType" : "text/csv",
         "derefUri" : '<base64>'
    }
    headers = {
        'authorization': "ZGFuaWVsZ29sZG1hbjpTdGFybGlnaHQ0Ng== ",
        'accept': "application/vnd.whispir.message-v1+json",
        'content-type': "application/vnd.whispir.message-v1+json"
        }

    response = requests.post( url, data=payload, headers=headers, params=querystring)

    print(response.text)


def import_csv():
    i_file =  open('mock.csv', 'rt')
    d_file = csv.DictReader(i_file)
    fieldnames = d_file.fieldnames
    return [row for  row in d_file], fieldnames


# ['dzgoldman@wesleyan.edu', 'dannyg9917@gmail.com']
def send_with_attachments(recipients, message):
    fromaddr = info.gmail
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = "SUBJECT OF THE EMAIL"

    body = "TEXT YOU WANT TO SEND"

    msg.attach(MIMEText(body, 'plain'))

    filename = "weather_year.csv"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, info.gpassword)
    text = msg.as_string()
    server.sendmail(fromaddr, recipients, text)
    server.quit()
