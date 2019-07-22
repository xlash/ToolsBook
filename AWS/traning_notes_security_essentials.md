Course 3
## Logging
	1. Security
	2. Event
	3. API calls
	4. Configuration Changes

Log Storage Regulations
PCI DSS 1 year
HIPAA 6 years

### Store logs in 
	1. S3 Bucket
		Service Access logs
		[ ] Access logs are not active by default
	2. Glacier
	3. CloudWatch Logs
	4. EBS
	5. EFS

Service logging
	a.	CloudTrail
		AWS APIs
		APIs
	b. S3 logs can go to the same or different bucket
	c. Elastic Load Balancing
		Need to enable access logs for ELB, define name of target bucket
		Attach a bucket policy allowing ELB write permission
		Define lifecycle rules to archive or delete
	d. Amazon CloudFront
		Logs available from web and RTMP
		Disabled by default
	e. Amazon CloudWatch Logs
	f. Amazon CloudWatch Events
## Encryption

## Network Security