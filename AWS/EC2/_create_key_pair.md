ssh-keygen -t rsa -C "my-key" -f ~/.ssh/my-key

aws --profile master_of_puppet --region us-east-1 ec2 \
	create-key-pair \
	--key-name "KEYPAIR_xss_server_1" \
	| \
	jq -r ".KeyMaterial" > ~/.ssh/KEYPAIR_xss_server_1.pem

