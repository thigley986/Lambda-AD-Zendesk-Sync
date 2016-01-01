#Sync from LDAP to S3 Bucket Engine
$DomainName = Get-ADDomain | Select -ExpandProperty Name
Get-ADUser -Filter {Enabled -eq $true} -properties DisplayName, EmailAddress, OfficePhone| select DisplayName, EmailAddress, OfficePhone | ConvertTo-Json | New-Item c:\zendesk_sync\active_users\$DomainName.json -type file -force
