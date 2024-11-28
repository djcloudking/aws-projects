import boto3

def create_group(group_name):
    # Initialize the IAM client
    iam = boto3.client('iam')
    
    # Create a new group
    response = iam.create_group(GroupName=group_name)
    
    print(response)

# Example Usage
create_group(group_name="dj-group")
