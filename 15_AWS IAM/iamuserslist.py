import boto3

def list_users():
    iam = boto3.client("iam")
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response["Users"]:
            print(f"Username: {user['UserName']}, Arn: {user['Arn']}")

# Call the function to list all users
list_users()
