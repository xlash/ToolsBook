# Get EC2 instance meta-data from ec2 shell

curl http://169.254.169.254/latest/meta-data/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

wget http://s3.amazonaws.com/ec2metadata/ec2-metadata

/latest/meta-data/iam/security-credentials/
then
/latest/meta-data/iam/security-credentials/{ACCOUNT_NAME}
can provide an access keys 
```
{
  "Code" : "Success",
  "LastUpdated" : "2019-04-08T22:26:54Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIA6GG7PSQGZYJSXC6C",
  "SecretAccessKey" : "whQ6V4LsU1YdssZsMHN3tXtpiAUxQRdQsWIAeTFA",
  "Token" : "AgoJb3JpZ2luX2VjEIf//////////wEaCXVzLXdlc3QtMiJHMEUCIE9gqNMe7g26G4C+mWHnLiWZCxZUifD1WwkHkavqDbbKAiEAt+ZdRoQBfXo9USR1gZLLGHCmlUrXvPUfKKjV5u8Vrzkq2gMIUBAAGgw5NzU0MjYyNjIwMjkiDBRf4vHU+GU1dnvjZyq3AxgaPpPxR1jsVt6idrg0AKvTAOza2nBruvHNpP1GOCpRYR56fW83oW0/EBHee7b4yG149GMrLu6YXLGjNomIdNVXqVw0cI2K+OXnKe2CDLlbosY6eY/OY914dQu9S9LuDuKTwSXnWGPDNy96qEeONaZ5VAXLrj2JM8euEwL9Ad2cfkRcH46DfbrL5uhBZBQyvw1OXN+DqcpX7LUxVUl4GMDlqAn3ldOxugp8KUxB7GQoD1piA/CdnMTtMvblOGTL+SQNtaeTy6XyWp3vKaZZzOJulte55BzMtWmBWapS9lgY9LQ/o/dKp0ef+eXezO8A3EywYUpVrkRGQeqC+srugvkcxYJGyRbk3mVtySPMZtj22xGNWZ5Zanjn/V15s5YwjPjb72tBXOELLcC/WhzymFKNcIsAsSIrtlDDor4nT2z7GaskT0qWNyxPQf/GJiVikgaBBWaJvQFqIR14lRBON5Sd36ci7v+ixlAtGO57/jua8S0DnzgrZrkcp5KjrmZDT1TLm0V9AjgyeHvk/Z+E+Z+ftJcWdkW2+XDxowUImlLv+7OMAsCXi1GcFPXDf/ycOPWkeSLLv34wtJWv5QU6tAHNxvWYli/s15drTWdNPNh7y77RzCl+8zUKABNrgamyCL/7QetZwbP91EAXUCpuDCorX3c6q4rXQgPnZmRI0rtjhjTVGbTtzpu/lpby+RP1c/NZQgDv5NMWH6B2LKomYdrJdEfYl40R+GTI2h/+vJCiQ/VlY1pXt/XDFG3pbmQjId4XiHZCsJiLSOWAoYhizWzN9TOPc0Qyq+3YnfZwJ9X7eLcng3ZpX4sLw4KZVR1sbwmVlKc=",
  "Expiration" : "2019-04-09T04:43:22Z"
}

```
```
ami-launch-index: 0
ami-manifest-path: (unknown)
ancestor-ami-ids: not available
block-device-mapping:
         ami: /dev/xvda
         ebs2: sdb
         root: /dev/xvda
instance-id: i-0c7ff93336b5685da
instance-type: t2.micro
local-hostname: ip-172-31-36-66.us-west-2.compute.internal
local-ipv4: 172.31.36.66
kernel-id: not available
placement: us-west-2b
product-codes: not available
public-hostname: ec2-34-221-235-54.us-west-2.compute.amazonaws.com
public-ipv4: 34.221.235.54
public-keys:
keyname:US-west-2a-Ubuntu_2019_04
index:0
format:openssh-key
key:(begins from next line)
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCeKrTDyBBr+SEsnCWOjx/HOGpqc73uS7nmoFyoz1rG6PwA0r48pjl8TuPUkGuQBxDZjRX95mqCznYUVE9sUUhvoNAJi24Dahoc9bMolWpItQKCTBbpl9BXmpd/MwgoCaTXXBd/zSkG6vlBkDmtUnJKSY1+WSHo3MMOtlnMQ54jad3ElS74iIm9Fn11UojQ70DCZJ6iBxjlkAHx4BrCsJuXy/3o/2CtIGGoFCvXEEBLc+fsXIUVVpZZueLFNotM+/NobE8+j7WxuJrXkrS/t/xSI1Oba2NjgqQcH9VTQSKdSB/nFklT9nUvjsN8Eb7Ior1SbAVmV4hS+A7z2zaQzXyr US-west-2a-Ubuntu_2019_04
ramdisk-id: not available
reservation-id: r-03e0d11f30b3eecc7
security-groups: launch-wizard-1

```
