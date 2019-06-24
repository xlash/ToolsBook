[GPO Info] (https://social.technet.microsoft.com/Forums/windowsserver/en-US/0453271c-bf23-461b-b001-7f353d293d08/enforced-or-not-in-group-policy-object)

Order of GPO being applied 

Local system policies first,
	 then policies on the Active Directory Domain level, 
	 	then policies on the Active Directory Site level and 
	 		then the policies for all the Organization Units the computer and user are members of

Link enabled : GPO is enforce
Enforced: GPO value cannot be overriden at another level.

[]
# Bitlocker
	[] Verify if bitlocker is enforced
	[] Usage of PIN (Needed for a stronger security than TPM only.)


# Password policy
Account Policies/Kerberos Policy
	Policy	Setting
		Enforce user logon restrictions	**Enabled**
		Maximum lifetime for service ticket	**x minutes**
		Maximum lifetime for user ticket	**x hours**
		Maximum lifetime for user ticket renewal	**x days**
		Maximum tolerance for computer clock synchronization	**x minutes**

# Verify Windows Remote Management (WinRM) IP restrictions

# Restrict network communications to non-domain networks, when connected to a domain one. (Dual homing)
(https://superuser.com/questions/112585/how-can-i-disable-wifi-when-computer-is-connected-to-lan-with-wire-using-gpo)
	 Open the Group Policy Object (GPO) for the setting that's linked to the required domain or OU.
	 Navigate to \Computer Configuration\Policies\Administrative Templates\Network\Windows Connection Manager.
	 Double-click Prohibit connection to non-domain networks when connected to domain authenticated network, and select the Enabled setting.

# Certificate enrollment and deployment on endpoint
	Policies
		Windows Settings
			Security Settings
				Public Key Policies/Certificate Services Client - Auto-Enrollment Settings
					Policy	Setting
					Automatic certificate management	Enabled
					Option	Setting
					Enroll new certificates, renew expired certificates, process pending certificate requests and remove revoked certificates	Enabled
					Update and manage certificates that use certificate templates from Active Directory	Enabled


For additional information about individual settings, launch the Local Group Policy Object Editor.