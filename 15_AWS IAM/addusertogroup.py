import boto3

def add_user_to_group(username, group_name):
    # Initialize the IAM client
    iam = boto3.client('iam')
    
    # Add the user to the specified group
    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )
    
    print(response)

# Example Usage
add_user_to_group(username="djcloud", group_name="dj-group")
