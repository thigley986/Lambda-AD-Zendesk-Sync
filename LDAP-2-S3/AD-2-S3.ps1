#Sync from Active Directory to S3 Bucket Engine
Import-Module "C:\Program Files (x86)\AWS Tools\PowerShell\AWSPowerShell\AWSPowerShell.psd1"

$accesskey = "AWS Access Key"
$secretkey = "AWS Secret Key"
$bucket = "AWS Bucket Name"

Set-AWSCredentials -AccessKey $accesskey -SecretKey $secretkey

try
    {
        Import-Module ActiveDirectory
        $DomainName = Get-ADDomain | Select -ExpandProperty Name
        echo $env:temp\zendesk_sync\active_users
        New-Item $env:temp\zendesk_sync\active_users -type directory -force
        Get-ADUser -Filter {(Enabled -eq $true) -and (EmailAddress -like "*" )} -properties DisplayName, EmailAddress, OfficePhone| select DisplayName, EmailAddress, OfficePhone | ConvertTo-Json | New-Item $env:temp\zendesk_sync\active_users\$DomainName.json -type file -force

        echo "Writing to Amazon S3 Bucket"
        Write-S3Object -BucketName $bucket -Key "$DomainName.json" -File $env:temp\zendesk_sync\active_users\$DomainName.json
    }
        catch [Exception]
    {
        echo $_.Exception.GetType().FullName, $_.Exception.Message
    }
