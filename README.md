# Lambda-AD-Zendesk-Sync
Sync Active Directory users and details to ZenDesk

The purpose of this project is to sync Active Directory users and user information to ZenDesk.  The methodology will rely upon the following:
  - Powershell Script to Retrieve Active Directory users and Details
  - Put the Active Directory user details to a specified S3 bucket
  - Lambda function to sync S3 bucket data to ZenDesk users
