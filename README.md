# Lambda-AD-Zendesk-Sync
Sync Active Directory users and details to ZenDesk

The purpose of this project is to sync Active Directory users and user information to ZenDesk.  The methodology will rely upon the following:
  - Powershell Script to Retrieve Active Directory users and Details
  - Put the Active Directory user details to a specified S3 bucket
  - Lambda function to sync S3 bucket data to ZenDesk users

Requirements
  - AWS Lambda Environment (Python 2.7) per ZenDesk Instance
  - AWS S3 Bucket per ZenDesk Instance
  - AWS Toolkit for Windows installed on Domain Controller
  - PowerShell v3 or Above

Legacy Servers may upgrade PowerShell to v3 by installing .NET Framework 4.5 and the Windows Management Framework 3.0 here:
  - Windows 2008 R2: https://www.microsoft.com/en-us/download/confirmation.aspx?id=34595&6B49FDFB-8E5B-4B07-BC31-15695C5A2143=1

  - Windows 2008 (64-bit): https://download.microsoft.com/download/E/7/6/E76850B8-DA6E-4FF5-8CCE-A24FC513FD16/Windows6.0-KB2506146-x64.msu
