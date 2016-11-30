''' Miscelaneous application functions, that deal with higher level functionality (sending email, making API requests, etc)'''

import requests, secrets, json

base_url = "https://api.whispir.com/workspaces/1992E463B84A38AF/%s"
auth = (secrets.user, secrets.whispir_password)
querystring = {"apikey": secrets.key}

def send_messages ( encoded_csv, template_id):
    ''' Meta function: sends out text messages emails to contacts.
        Uses create_resource, get_resource_id, and post_messages
        param encoded_csv (bytes): base64 encoded JSON object of file
        param template_id (string): id of template to use for messages
        returns: response object of final post request
    '''
    response = create_resource( encoded_csv)
    resource_id = get_resource_id(response)
    return post_messages(resource_id, template_id = template_id)


def create_resource( encoded_csv):
    '''
    Sends data to Whispir API. Uses requests module.

    param encoded_csv (bytes): csv file B64 encoded
    returns: HTTP response object
    '''
    url = base_url % ('resources')

    payload = {
      "name" : 'Resource for CCI Template',
      "scope" : "private",
      "mimeType" : "application/json",
      "derefUri" : encoded_csv
      }
    headers = {
        'accept': "application/vnd.whispir.resource-v1+json",
        'content-type': "application/vnd.whispir.resource-v1+json"
        }
    response = requests.post( url,auth = auth,json = payload,headers= headers,params= querystring)
    print('resource creation status_code: ', response.status_code)
    return response


def get_resource_id(res):
    ''' parse out resource response to get resource ID'''
    url = res.json()['link'][0]['uri']
    resource_id = url.split('resources/')[1].split('?apikey')[0]
    return resource_id


def post_messages(resource_id, template_id= None):
    ''' Uses already existing resource and template to send out sms
    param resource_id (string): id of resource to use on Whispir API
    param template_id (string): id of template to use on Whispir API

    '''
    url = base_url % ('messages')
    headers = {
                'accept': "application/vnd.whispir.bulkmessage-v1+json",
                'content-type': "application/vnd.whispir.bulkmessage-v1+json"
                }
    payload = {
    "resource" :{
    "resourceId" : resource_id,
    "smsMappingField" : "mobile",
    "emailMappingField" : "email"
    ,"voiceMappingField" : ""
        },
        "messageTemplateId": template_id
    }

    response = requests.post(url,json = payload,auth = auth,headers = headers,params = querystring)
    print('message post status code:', response.status_code)
    return response
