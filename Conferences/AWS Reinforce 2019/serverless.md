George Mao
SErverless specialist
@georgemao

SDD401 : Securing Enterprise Grade Serveless Application

# Security principles
## LEAST PRIVILEGE
minimize scoped policies per resource, removed action*

## Clean code
	1. Ensure no creds, username, password in code.
		Get ephemeral permissions
		Store in AWS secrets manager 
	2. Lambda function should be small
		Group them by purpose
			==> Single purpose ACTION/HTTP verb. A lambda for Get, post, put, etc.

# Security threats
## DDoS, XSS from the web
Cloudfront to API Gateway : DDoS, CORs
## Injection problems in lambda
## Database : Data loss

## Use OpenIDConnect for identity and authorization at every layer.

## Use conditions in IAM policies
	for example, restrict VPC source
	or restrict aws:SourceIp :: CIDR
	aws:PrincipalTag
		username
		ResourceTag
		UserAgent
		PrincipalOrgId
		SecureTransport
		CurrentTime

## Privileges
[++] Lambda Environment Variables are injected at runtime from KMW.
[+] Dynamo DB supports encryption at rest, would be worth investigation for secrets storing
[++] Secrets manager
[+] Use IAM authentication

## Audit your configuration
Through AWS Config