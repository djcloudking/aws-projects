import boto3
import json

def create_iam_role():
    # Initialize the IAM client
    iam = boto3.client("iam")

    # Trust relationship policy for the role
    assume_role_policy_document = json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "glue.amazonaws.com"  # AWS Glue assumes this role
                },
                "Action": "sts:AssumeRole"
            }
        ]
    })

    # Create the role
    response = iam.create_role(
        RoleName="glueS3CrawlerRole",
        AssumeRolePolicyDocument=assume_role_policy_document
    )

    print(f"Created Role: {response['Role']['RoleName']}")
    return response["Role"]["RoleName"]

# Example Usage
role_name = create_iam_role()
print(f"New IAM Role: {role_name}")
