# API Challenge


## Details
2. Mission & Requirements
a. You need to configure the current API and new secure API that Akira created last night. The new secure API was only created, so please complete the API Gateway configuration.
b. Please don't use the "Use proxy integration" setting when you configure secure API(If you enable it, the backend application will not work well.)
[c]. Akira also generated 2 new API keys last night, but he did not configure them. Please configure them. The current API MUST support both keys(existing and new) and the new Secure API MUST support only the new API key
d. Current API is only allowed to access from Current VPC application. Please configure access control using API configuration.
e. Secure API is only allowed to access from Secure VPC. Secure VPC is not attached Internet Gateway, so please configure Private API.

## Write-up


└──╼ $aws sts get-caller-identity
{
    "UserId": "AROAQR5DHBGHBLIGTZXYW:MasterKey",
    "Account": "038460131726",
    "Arn": "arn:aws:sts::038460131726:assumed-role/TeamRole/MasterKey"
}


2. Attach API policy to EEOverlord user through Dashboard


3. Will add additionnal permissions
 User: arn:aws:sts::038460131726:assumed-role/TeamRole/MasterKey is not authorized to perform: apigateway:GET on resource: arn:aws:apigateway:eu-central-1::/restapis
==> Add to attach policy to role assumed : Policy API-Developer-eu-central-1 has been attached for the TeamRole.

```issue
User: arn:aws:sts::038460131726:assumed-role/TeamRole/MasterKey is not authorized to perform: apigateway:GET on resource: arn:aws:apigateway:eu-central-1::/apis
```

4. Log out and back in fixed the issue


5. Associated SecureAPIKey to SecureUsagePlan
Added new API key to CurrentUsagePlan
==> Fullfils requirement 2c

6. Configured the Policies for IP whitelisting for Secure and Regular API

7. Deploying APIs

Replace Resource Store in Systems Manager 
Secure key value from Zzk5NXl6eXB5ajAzODQ2MDEzMTcyNg==
Current key from Zzk5NXl6eXB5ajAzODQ2MDEzMTcyNg==
Secure End point from https://g995yzypyj.execute-api.eu-central-1.amazonaws.com/prod/







{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "arn:aws:execute-api:/*",
            "Condition": {
                "StringEquals": {
                    "aws:sourceVpc": "vpc-0dbdc07d7e33cf607"
                }
            }
        }
    ]
}





{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "arn:aws:execute-api:*",
            "Condition": {
                "StringEquals": {
                    "aws:sourceVpc": "vpc-032cdc4172a43c53e"
                }
            }
        }
    ]
}