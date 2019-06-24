# Request Read and Security Reader role

# Azure Cannot verify 2FA settings and external Identity without Administrator privileges.

	(https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/directory-assign-admin-roles)
	External Identity Provider Administrator
	Configure identity providers for use in direct federation.

	Actions	Description
	microsoft.aad.b2c/identityProviders/allTasks	Read and configure identity providers in  Azure Active Directory B2C.

Security Center provides such recommendations, but not without the standard tier
	+Enable MFA for privileged accounts on your subscription
	+Remove external accounts with write permissions from your subscription
	+Remove privileged external accounts from your subscription
	(https://docs.microsoft.com/en-us/azure/security-center/security-center-identity-access)