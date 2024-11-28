import boto3

def create_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print(response)

# Create a username called djcloud
create_user("djcloud")

