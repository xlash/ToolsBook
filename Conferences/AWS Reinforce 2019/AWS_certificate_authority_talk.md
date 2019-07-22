Echo device each have a certificate (check online document)

Replace software/server-based CAs

Replace offline root CA
Complement an existing root CA
	delegate a sub hierarchy?

## Hardening and configurations recommendations
Cloudwatch alarms and metrics, notifications
	Certificate issuance

CloudTrail logging of API calls
Revocation configuration
Key types and sizes
	RSA 2018, 4096, ECDSA P256, ECDSA P384

After lifetime, good practice replace with a new CA

## Best practices
(Picture taken 2019-06-26 16:46 )

Separate AWS accounts for access. (Account separation)

Disabling a CA allows CRL to work, but not to issue new certs. 
Role separation (enabling or not the CA, and issuing certs) for root or top level

## CA Hierachy recommendations
Limit height
	==> Performance
Use  minimum size
Use path length constrain to limit CA height

Backed by a L3 HSM, shared HSM.