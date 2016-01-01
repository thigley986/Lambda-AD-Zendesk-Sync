#Sync from LDAP to S3 Bucket Engine
Get-ADUser -Filter {Enabled -eq $true} -properties DisplayName, EmailAddress, OfficePhone| select DisplayName, EmailAddress, OfficePhone | ConvertTo-Json | New-Item c:\zendesk_sync_tools\active_users.json -type file -force
