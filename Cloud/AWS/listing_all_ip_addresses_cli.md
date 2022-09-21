# Listing all ip addresses using the AWS CLI

**Description:** This entry will describe how to list all ip addresses in your account using the AWS CLI by region. This is useful for reporting.

**Requirements:** AWS CLI

**Provider:** AWS (Amazon Web Services)

**Service:** EC2

## Configuring the CLI

```
aws configure
```

Use the prompts to enter your credentials, region, and preferred output type


## Using the CLI to list all ip addresses

```
aws ec2 describe-instances --region <region> --query="Reservations[].Instances[].PublicIpAddress" | jq -r ".[]"
```

Use the AWS CLI to list all ip addresses on ec2 instances in a certain region. The piping to jq is optional
  
## References
* https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
* https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
* https://docs.aws.amazon.com/cli/latest/reference/
* https://stedolan.github.io/jq/download/
