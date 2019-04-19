#Script readable
while read p; do 
	echo "REGION=$p"; 
	aws --profile adv_270023481769 ec2 describe-subnets --region "$p" --subnet-ids subnet-00eaf849 ; 
done < /ToolsBook/AWS/EC2/_regions.list

#1-liner version
#while read p; do echo "$p"; aws --profile adv_270023481769 ec2 describe-subnets --region "$p" --subnet-ids subnet-00eaf849 ; done < /ToolsBook/AWS/EC2/_regions.list
