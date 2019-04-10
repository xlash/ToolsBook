1- Completly open bucket

# Find Region
```bash
dig +nocmd flaws.cloud any +multiline +noall +answer
# Returns:
# flaws.cloud.            5 IN A  54.231.184.255

nslookup 54.231.184.255
# Returns:
# Non-authoritative answer:
# 255.184.231.54.in-addr.arpa     name = s3-website-us-west-2.amazonaws.com
```
# Using AWS_CLI on an insecure bucket 
aws s3 ls  s3://flaws.cloud/ --no-sign-request --region us-west-2


2. Bucket open to authenticated users only (from any AWS accounts)
```
aws s3 --profile master_of_puppet ls s3://level2-c8b217a33fcf1f839f6f1f73a00a9ae7.flaws.cloud
```
