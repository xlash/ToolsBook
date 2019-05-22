# Domain controllers Hardening

## Network ports
Ensure the following list of ports are open, but not more.

	UDP Port 88 for Kerberos authentication
	UDP and TCP Port 135 for domain controllers-to-domain controller and client to domain controller operations.
	TCP Port 139 and UDP 138 for File Replication Service between domain controllers.
	UDP Port 389 for LDAP to handle normal queries from client computers to the domain controllers.
	TCP and UDP Port 445 for File Replication Service
		445 (To allow Sysvol access)
	TCP and UDP Port 464 for Kerberos Password Change
	TCP Port 3268 and 3269 for Global Catalog from client to domain controller.
	TCP and UDP Port 53 for DNS from client to domain controller and domain controller to domain controller.
	https://www.experts-exchange.com/questions/29021114/Windows-firewall-ports-to-open-on-memeber-server-for-domain-controllers.html

	TCP 1025-5000 49152-65535: Active Directory  https://www.tevora.com/secure-domain-controllers-next-gen-firewalls/


## Use a separate device for DC administration than for sysadmin tasks.
	https://www.zdnet.com/article/microsoft-recommends-using-a-separate-device-for-administrative-tasks/

## Domain accounts on a separate forest, that cannot access Internet.