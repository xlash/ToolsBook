# Will list all snapshots in that AWS accounts
[REQUIRE ACCESS]
aws ec2 describe-snapshots

Capture snapshot ip


## 2. Copy a snapshot to your instance

aws --profile master_of_puppet ec2 create-volume --availability-zone us-east-1a --region us-east-1  --snapshot-id  snap-0b49342abd1bdcb89

