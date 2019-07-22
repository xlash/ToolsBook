Vinod Madabushi
AWS Enterprise Architect
Secure Active Directory with AWS

Slides will be posted on slideshare and youtube recording
2019-06-25 11hr30


Why deploy AWS in IaaS
Support Windows workloads running in AWS
Reduce latency for application and resources
Managed services

2 options
	1- Self-managed EC2 
	2- AWS-managed Microsoft AD

AWS Managed AD
	Set-up one-way or two-way trust
	Objects are all created in AWS Managed AD (reousrces, credentials)
	Need delineation between on-premises and AWS environments
	Need native integration with RDS FSx Single Sign-On

AWS master account  
	AWS organizations      

Shared services account 
       Domain Controllers
       (separate account from other business units, simpler in a different account)
       	If there are multiple teams operating in a single account, consider using tab-based policies to restrict acces
       		Restrict (only to AD admin) access to Amazon EC2 start/stop/terminate
       		Restrict access to Amazon EBS volumes/snapshots  (do not allow attach and copy to another instance)

Log archive account
	Aggregate AWS CloudTrail and AWS Config logs

Security Account
	Amazon GuardDuty (master)



Domain Controllers in private subnets.
Multiple AZ for availability
Avoid using NACLS to filter Active Directory ports unless absolutely necessary (ephemeral ports can be tricky)
Routing table can be utilized as a network control mechanism

Internet Resolving:
1- Internet Name Resolution from the DCs. Point them to Route 53 .2 resolver (there is a limit of performance)
2- Point to Public subnet DNS server you might already have
3- [Less recommended, cuz it goes to the Internet directly] NAT Gateway in the public subnet to initiate outbound connection. (Inbound should be blocked)

CloudHSM store your CMK (Custom Key Store)

[See considerations slides]
DloudTrail AWS account and key change alerts
Monitor DC for availability


AWS Managed AD is single tenant. Your DCs only contain your data
AWS employees don't have access to customer's domain admin creds. (Under automated control)
Logs delivered to cloudwatch
Delegated admin access using predefined users, groups and OUs (Just in time, limited permissions, no domain admin creds)

Limit access [See slides]