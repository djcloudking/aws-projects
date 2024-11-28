import boto3

def attach_user_policy(policy_arn, username):
    # Initialize the IAM client
    iam = boto3.client("iam")
    
    # Attach the policy to the specified user
    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)

# Example Usage
attach_user_policy(
    policy_arn="arn:aws:iam::xxx:policy/testDynamoDBPolicy", 
    username="djcloud"
)
