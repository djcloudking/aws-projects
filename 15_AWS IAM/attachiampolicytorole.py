import boto3

def attach_iam_policy(policy_arn, role_name):
    # Initialize the IAM client
    iam = boto3.client("iam")
    
    # Attach the policy to the role
    response = iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    
    print("Policy attached successfully.")
    print(response)

# Example Usage
attach_iam_policy(
    policy_arn="arn:aws:iam::aws:policy/AmazonS3FullAccess",
    role_name="glueS3CrawlerRole"
)
