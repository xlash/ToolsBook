#Script readable

while IFS=',' read -r name id tenant_id; do 
        if echo $name | grep -qE '^#'; then
                continue
        fi
	echo "Azure Subscription Name=$name ID=$id"; 
	az account set --subscription $id                                                                                                     
	sleep 2  
	python /home/gnm/Development/ScoutSuite/scout.py --provider azure --tenant $tenant_id --subscription $id --cli --report-name "$name" -f
done < subscriptions_list.csv

#1-liner version
#while read p; do echo "$p"; aws --profile adv_270023481769 ec2 describe-subnets --region "$p" --subnet-ids subnet-00eaf849 ; done < /ToolsBook/AWS/EC2/_regions.list

