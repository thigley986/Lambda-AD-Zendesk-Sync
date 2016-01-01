#Sync from Lambda function to Zendesk

#Amazon S3 Bucket to Zendesk Import Process

from __future__ import print_function
import sys
from zdesk import Zendesk
from zdesk import get_id_from_url
import boto3
import collections

#Define ZenDesk API Information
config = {
    'zdesk_email': 'zendesk_email@zendesk.com',
    'zdesk_password': 'zendesk_password_or_token',
    'zdesk_url': 'URL',
    'zdesk_token': True
}

#Create client with S3
s3 = boto3.client('s3')

#Create ZenDesk Connection
zendesk = Zendesk(**config)

def lambda_handler(event, context):
    #List User
    users = zendesk.users_list().get('users', [])
    print("Listing Current ZenDesk Users")

    for user in users:
        name = user['name']
        print(name)

    #Create User
    print("Adding Users")
    user_name = "Test"
    user_email = "Test@Test.com"
    user_phone = "(222) 222-2222"

    new_user = {
        'user': {
            'name': user_name,
            'email': user_email,
            'phone': user_phone,
        }
    }
    try:
        result = zendesk.user_create_or_update(data=new_user)

        #Print Generated User ID
        user_id = get_id_from_url(result)
        print(user_id)
    
    except Exception, e:
        print ("Error Encountered:")
        print (e)

