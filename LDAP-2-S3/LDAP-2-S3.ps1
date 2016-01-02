#Sync from LDAP to S3 Bucket Engine
try
    {
        Import-Module ActiveDirectory
        $DomainName = Get-ADDomain | Select -ExpandProperty Name
        Get-ADUser -Filter {Enabled -eq $true} -properties DisplayName, EmailAddress, OfficePhone| select DisplayName, EmailAddress, OfficePhone | ConvertTo-Json | New-Item c:\zendesk_sync\active_users\$DomainName.json -type file -force
    }
        catch [Exception]
    {
        echo $_.Exception.GetType().FullName, $_.Exception.Message
    }
