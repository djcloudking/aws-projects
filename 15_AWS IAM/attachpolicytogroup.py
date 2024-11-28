import boto3

def attach_group_policy(policy_arn, group_name):
    # Initialize the IAM client
    iam = boto3.client("iam")
    
    # Attach the policy to the specified group
    response = iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
    
    print(response)

# Example Usage
attach_group_policy(
    policy_arn="arn:aws:iam::xxx:policy/testDynamoDBPolicy",
    group_name="dj-group"
)
