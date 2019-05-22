# Objective deanonymize a SERVER hosted on TOR (.onion)

Set a Via Headers
Set proxy Headers

Set HTTP Method to STRACE


Set WWW-Authenticate headers with realm maybe?

Basic realm-
Negociate realm=
NTLM realm=

# Set a TOR vpn forwarder local with ubuntu
install tor
netstat -an | grep 9050

## Confirm TOR is in use.
wget -qO - https://api.ipify.org       
184.151.111.234%                                                                                                                                                                                              ➜  ~ torsocks wget -qO - https://api.ipify.org       
torsock wget -qO - https://api.ipify.org       
195.176.3.19%        

# Set-up burp to listen to browser request, and in User Options tab, forward to a local SOCK proxy on 127.0.0.1 9050 and forward DNS.
Browser request should be redirected to burp through tor

