# Lambda-AD-Zendesk-Sync
Sync Active Directory users and details to ZenDesk

The purpose of this project is to sync Active Directory users and user information to ZenDesk.  The methodology will rely upon the following:
  - Powershell Script to Retrieve Active Directory users and Details to a JSON file
  - Put the Active Directory user details to a specified S3 bucket
  - Lambda function to sync S3 bucket data to ZenDesk users

Requirements
  - Zendesk Account with Administrator-level access
  - AWS Lambda Environment (Python 2.7) per ZenDesk Instance
  - AWS S3 Bucket per ZenDesk Instance
  - AWS Tools for Windows PowerShell installed on Domain Controller (https://aws.amazon.com/powershell/)
  - PowerShell v3 or above set to Unrestricted execution mode
  - Zdsk API for Python by Brent Woodruff (https://github.com/fprimex/zdesk)
  - Boto3 AWS SDK for Python (https://github.com/boto/boto3)
  - pip Package Manager (for installation of third-party dependencies)

Legacy Servers may upgrade PowerShell to v3 by installing .NET Framework 4.5 and the Windows Management Framework 3.0 here:
  - Windows 2008 R2: https://www.microsoft.com/en-us/download/confirmation.aspx?id=34595&6B49FDFB-8E5B-4B07-BC31-15695C5A2143=1

  - Windows 2008 (64-bit): https://download.microsoft.com/download/E/7/6/E76850B8-DA6E-4FF5-8CCE-A24FC513FD16/Windows6.0-KB2506146-x64.msu

Installation (Lambda)
  - Create an AWS S3 bucket
  - Create a ZenDesk API token (https://developer.zendesk.com/rest_api/docs/core/introduction#api-token)
  - Download Lambda-2-Zendesk.py to a folder
  - Modify Lambda-2-Zendesk.py to include S3 bucket and ZenDesk configuration
  - Download Zdsk API and dependencies to the same folder using command: pip install requests pyopenssl ndg-httpsclient pyasn1 zdesk -t /path/to/project-dir
  - Download zdesk_api.py and replace the default zdesk_api.py file in the zdesk folder
  - ZIP the files in the directory (not the directory) and upload to an AWS Lambda Python 2.7 function
  - Name your Lambda function handler Lambda-2-Zendesk.lambda_handler
  - Choose S3 Execution Role, Create a new IAM role, and set the execution policy to the IAM POLICY document in the Lambda project folder
  - Set Lambda function timeout to 300 seconds
  - Set Event Source to the S3 bucket for ObjectCreated | json
  - (Optional) Set Event Source to S3 bucket for rate(1 hour)

Installation (Windows)
  - Install AWS Tools for Windows PowerShell
  - Create AWS IAM User with IAM POLICY document in the LDAP-2-S3 project folder
  - Download and modify AD-2-S3.ps1 to include S3 bucket Access Key, Secret Key, and Bucket
  - Schedule AD-2-S3.ps1 to run using Windows Task Scheduler or preferred RMM tool
