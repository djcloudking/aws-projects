import boto3

def update_user(old_user_name, new_user_name):
    iam = boto3.client('iam')
    # Update the user's name
    response = iam.update_user(
        UserName=old_user_name,
        NewUserName=new_user_name
    )
    print(response)

# Example: Renaming "djcloud" to "test-dj"
update_user("djcloud", "test-dj")