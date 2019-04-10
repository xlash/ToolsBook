# Create and install a new keypair on LINUX
```
aws --profile master_of_puppet ec2 create-key-pair --key-name US-west-2a-Ubuntu_2019_04  --region us-west-2 --query 'KeyMaterial' --output text > ~/.ssh/US-west-2a-Ubuntu_2019_04.pem
```
[https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-keypairs.html]
