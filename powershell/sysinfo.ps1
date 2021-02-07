#$Hello = "Hello Powershell"
function GetIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
    }


$IP = GetIP
$user = $env:USERDOMAIN
$Date = Get-Date
$this = $host.Version.Major

$Body = "This machine's IP is $IP. User is $env:username. Host name is $user. Powershell version $this. Today's Date is $Date. "
#Send-MailMessage -to "frewce@mail.uc.edu" -from "
Write-Output $Body
