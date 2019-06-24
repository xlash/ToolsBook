#SonicWall Hardening

##Allow Interface Trust

The Allow Interface Trust setting in the Add Zone window automates the creation of Access Rules to allow traffic to flow between the interface of a zone instance. For example, if the LAN zone has both the LAN and X3 interfaces assigned to it, checking Allow Interface Trust on the LAN zone creates the necessary Access Rules to allow hosts on these interfaces to communicate with each other.

==> Not problematic, unless many interfaces are set in the same zone.

# restrict SSH, HTTPS from network interfaces allowed to adminster
```bash
 egrep '(Interface Name .+)|(IPv[46] Settings.+)|(Interface [httpsh]{3,5}+ .+)' Sonicwall-techsupport.wri

Interface Name                                  : X#:V#                          
[IPv4 Settings]
IP Address                                      : X.X.X.X
Interface http Management                       : No                              
Interface https Management                      : Yes                             
Interface ssh Management                        : Yes                             
Interface ping Management                       : Yes                             
Interface snmp Management                       : Yes                             
Interface http User Login                       : No                              
Interface https User Login                      : Yes                             
Interface http Redirect Rule                    : Yes                             
Interface add DHCP Lease                        : No                              

[IPv6 Settings]
IPv6 Addresses:
	X:X:X:X:X::X	[Automatic]

Interface http Management                       : No                              
Interface https Management                      : No                              
Interface SSH Management                        : No                              
Interface ping Management                       : No                              
Interface snmp Management                       : No                              
Interface http User Login                       : No                              
Interface https User Login                      : No                              
Interface http Redirect Rule                    : Yes                             
``` 