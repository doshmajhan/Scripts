$ports = 21, 22, 25, 80, 161, 3306, 3389
$timeout = 3000

function bitshift ([long]$num, [int]$left) {
    return [math]::Floor($num * [math]::Pow(2,$left))
}

# Checks if a given IP address is located within the given subnet
function checkSubnet ([string]$cidr, [string]$ip){
    $network, [int]$subnetlen = $cidr.Split('/')
    $a = [uint32[]]$network.split('.')
    [uint32] $unetwork = (bitshift -num $a[0] -left 24) + (bitshift -num $a[1] -left 16) + (bitshift -num $a[2] -left 8) + $a[3]
    $mask = bitshift -num (-bnot [uint32]0) -left (32 - $subnetlen)
    $a = [uint32[]]$ip.split('.')
    [uint32] $uip = (bitshift -num $a[0] -left 24) + (bitshift -num $a[1] -left 16) + (bitshift -num $a[2] -left 8) + $a[3]
    $unetwork -eq ($mask -band $uip)
}

# Scans an IP address, pinging the host and trying to connect
# to the specified ports
function scan ([string]$ip){
	try {
		Test-Connection $ip -count 1 -ErrorAction Stop
	}
	catch {
		Write-Host "$env:computername `t$ip : Host is down" -ForegroundColor Red
	}
	foreach ($p in $ports) {
		$tcp = New-Object System.Net.Sockets.TcpClient
		
		$ErrorActionPreference = 'SilentlyContinue'
		$tcp.Connect($ip, $p)
		$ErrorActionPreference = 'Continue'
		
		if($tcp.Connected) {
			Write-Host "`t`tPort $p is open"
		}
		else{
			Write-Host "`t`tPort $p is closed"
		}
		$tcp.Close()
	}
}

if($args.length -ne 1){
	Write-Host "Please enter the IP address or subnet"
	Exit
}
$range = [string]$args[0]

# Check if IP address is in CIDR format or a singular address
if($range.contains("/")){
	$single = $false
	$sep = "/"
	$subnet = $range -split $sep
	$ip = $subnet[0]
	$cidr = $subnet[1]
}
else{
	scan -ip $range
	Exit
}

$nets = $ip.split('.')
$count = 3
$temp = ""

#Loop through the possible IP addresses and check if there in the subnet
foreach($n in $nets){
	for($i = [int]$n; $i -lt 255; $i++){
		$ip = $temp + $i
		for($x = 0; $x -lt $count; $x++){
			$ip = $ip +  ".0"
		}
		if(checkSubnet -cidr $range -ip $ip){
			scan -ip $ip
		}
		else{
			Break
		}
	}
	$temp = $temp + $n + "."
	$count = $count - 1
}