#Amazon S3 Bucket to Zendesk Import Process

from __future__ import print_function
import sys
from zdesk import Zendesk
from zdesk import get_id_from_url
import boto3
import json
import collections
from time import sleep

#Define S3 Bucket
bucket = "<BUCKET_NAME>"

#Define ZenDesk API Information
config = {
    'zdesk_email': '<ZENDESK_USER_EMAIL>',
    'zdesk_password': '<ZENDESK_USER_PASSWORD_OR_TOKEN>',
    'zdesk_url': '<ZENDESK_URL>',
    'zdesk_token': <'TRUE OR FALSE'>
}

#Define telephone country code (if Active Directory numbers formatted without code)
telephone_prefix = "1"

#Connect to S3 with Boto3
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

    #Find Most Recently Modified Active Users File from S3
    bucket_list = s3.list_objects(Bucket=bucket).get('Contents', [])
    print(bucket_list)

    for file in bucket_list:
        file_name = file['Key']

        try:
            object = s3.get_object(Bucket=bucket,Key=file_name)['Body']
            print(object)

        except Exception, e:
            print ("Error Encountered while downloading file.")
            print (e)
            exit()

        users = json.load(object)
        print(users)   

        #Create and Update User
        print("Creating and Updating Users")
        
        for user in users:
            user_name = user['DisplayName']
            user_email = user['EmailAddress']
            user_phone = user['OfficePhone']

            new_user = {
                'user': {
                    'name': user_name,
                    'email': user_email,
                    'phone': "%s%s" % (telephone_prefix, user_phone),
                }
            }

            try:
                print(new_user)
                result = zendesk.user_create_or_update(data=new_user)
                sleep(0.03)

                #Print Generated User ID
                user_id = get_id_from_url(result)
                print(user_id)
            
            except Exception, e:
                print ("Error Encountered:")
                print (e)

        print("Deleting File")
        s3.delete_object(Bucket=bucket,Key=file_name)
