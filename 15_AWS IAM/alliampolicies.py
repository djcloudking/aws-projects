import boto3

def list_policies():
    # Initialize the IAM client
    iam = boto3.client("iam")

    # Use a paginator to handle large result sets
    paginator = iam.get_paginator('list_policies')

    # Fetch policies scoped to the account (custom policies)
    for response in paginator.paginate(Scope="Local"):
        for policy in response["Policies"]:
            print(f"Policy Name: {policy['PolicyName']} ARN: {policy['Arn']}")

# Test the function
list_policies()
