# AWS Cost Optimization using Lambda function and boto3 library


Set up a Lambda function to help you save on storage costs by finding and deleting EBS snapshots that aren’t connected to any active EC2 instances.


## Create an EC2 instance

Check out this repository where I describe in detail how to create a EC2 instance.


## Verify EBS Volume

Go to the “Storage” section of your newly created EC2 instance. You’ll notice that this volume was automatically created when you set up the instance and is used as the root volume for your EC2 instance.


## Create a snapshot of the volume 

In your EC2 dashboard, go to snapshots, and click on create snapshot.


## Create a Lambda function

- Go to lambda dashboard. Click on create a function. Fill out the form, then click on create function.

- Copy the code for the lambda function from this repository: click here.
And paste it in lambda.py

- Click Deploy, then Test.

- Grant permission to allow Lambda to describe the ebs volumes.


## Execute Lambda and Verify result

- Go to Lambda dashboard and execute the code.

- You should get an error message.So please update the policy accordingly.

- There are no errors and our code is ready to be used.

- As intended, Snapshot is deleted when there is no existing EC2.

Voila! You’ve implemented Cost Optimization in your AWS environment. You used a Lambda function and boto3 library that delete EBS snapshots that aren’t connected to any active EC2 instances.