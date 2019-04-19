# Output a list of all the AWS regions like us-east-1, line feed separated
aws ec2 describe-regions --region us-east-1 | grep RegionName | gawk 'BEGIN{FS="\""} {print $(NF-1)}'
