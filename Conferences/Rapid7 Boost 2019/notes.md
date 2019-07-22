Rapid7 Boost conference

Corey Thomas CEO
	DevOps is driving the pace of change in the cloud
		+Flexible
		+Responsive
		+Distributed decision making

Security is not devops ready
	Siloed
	Decision making is very centralised to a few people only.

Embrace team members outside of security and outside of company

Develop and Delegate LEadership
	Remove leadership bottlenecks to increase speed and agility of decision making.


==================
4 reports from Rapid7 research
Sonar open data

HTTP Headers :
	expect-ct
	X-premitted-cross-domain

Q4 Threat Report 
	2018 Attack Map

################################ Labs

InsightVM 
https://r-7.co/2XyyLPS
	+new feature Assess your configuration "Cloud Configuration"
	CIS benchmarks for AWS foundations
	[ ] S3 MFA deleta disabled
	Exceptions can expired.

insigtConnect
	Orchestrate your workflow
		Auto-create tickets
		Notify in Slack or elsewhere
		270+plugins
		(approval flows, for example)

LAB InsightVM with Josh Frantz

	Deploy agent via lambda
		If company don't have a deployment infrastructure such as puppet, chef, SaltStack

Full Serverless site cloud.guru

SSM
	Run commands create a script in 
	/var/lib/amazon/ssm/[instanceID]/document/orchestration/[Another ID, SSM document id?]/[DocumentName]/_script.sh
	chmod is 700 with root

#########################################
Nadean Tanner Lead Technical Education Specialist (InsightIDR + Metasploit courses)
Teresa Copple Lead Security Consultant

InsightIDR
	Automation workflows :
		Deactivate a user during an IDR investigation.
		Create a service now ticket
		IDR does not kill the process by itself. Requires an investigation case, then user agent.
		Contain and kill a process
			Cannot prompt to the user
		Containment is done on the local firewall.
			not able to hook on another API
	Same agent for IDR and InsightVM

##############################
Spencer & Sidney 
InsightIDR Session B
Detection in a mix environment.

Security and 

Insight Connect :
	Workflow builder (pager duty, email, ticketing, slack)

Security Hub & Guard Duty