# Shows the adapters
ip link
# Set up dhcpclient
NETCTL CONFIG

Description='NorthSec CTF'
Interface=wlp2s0
Connection=wireless
Security=wpa-configsection
ESSID=NSEC
Auth8021X=yes
IP=dhcp

WPAConfigSection=(
'ssid="NSEC"'
'identity="team-2019-16"'
'ca_cert="/home/dom0/.local/northsec-ca.crt"'
'client_cert="/home/dom0/.local/team16.pem"'
'private_key="/home/dom0/.local/team16.key"'
'private_key_passwd="ospAwgOdFakViten"'
'key_mgmt=WPA-EAP'
'eap=TLS'
'group=CCMP TKIP'
'pairwise=CCMP TKIP'
)

/etc/dhcp.conf (ADD THIS SOMEWHERE if connectivity issues)

request subnet-mask, broadcast-address, time-offset, routers,
   domain-name, domain-name-servers, domain-search, host-name,
   dhcp6.name-servers, dhcp6.domain-search, dhcp6.fqdn, dhcp6.sntp-servers,
   netbios-name-servers, netbios-scope, interface-mtu,
   rfc3442-classless-static-routes, ntp-servers;

