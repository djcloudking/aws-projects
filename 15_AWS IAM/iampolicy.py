import boto3
import json

def create_iam_policy():
    # Initialize the IAM client
    iam = boto3.client('iam')

    # Define the policy document
    my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "dynamodb:GetItem",
                    "dynamodb:Scan",
                ],
                "Resource": "*"
            }
        ]
    }

    # Create the policy
    response = iam.create_policy(
        PolicyName='testDynamoDBPolicy',
        PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)

# Test the function
create_iam_policy()
