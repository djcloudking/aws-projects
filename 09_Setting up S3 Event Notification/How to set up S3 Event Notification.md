# S3 Event Notification

In this short tutorial, I will show you how to set up S3 Events Notification. 

## Background

Amazon S3 Event Notifications enable you to receive notifications when certain events happen in your S3 bucket. These events can include object creation, deletion, and more. 

# Prerequisite

For this tutorial, you need an AWS account. Set up a Free-Tier account www.aws.amazon.com/free.


## Steps

To set up S3 event notifications, you typically follow these steps: 


### Step 1: Create S3 bucket or use an existing bucket

- Log in to your AWS account.

- Go to S3 dashboard. 

- Click on Create bucket. 

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/0ba3aaa8-eb57-4d6d-b21f-af26b3590172)


- Now select the AWS region of your choice. Add a unique name for your S3 bucket. 

- Leave the configuration of other fields by default. Then click on create bucket. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/ff68fa75-fb93-4ec3-8aca-afec5b473b29)
 

### Step 2: Add a file to your bucket

- Upload a file in to S3. [Read this article](https://medium.com/@djakkone/aws-skills-challenge-2-storage-s3-16025c21c9b2) where I described how to upload a file to S3 bucket. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/3e964e56-f26f-4633-9896-45dfdc0e48f7)

 
### Step 3: Configure your event notifications

- Select your bucket and click on property. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/77423b9e-3a45-484e-8d84-b58bf88ba340)

 
- Scroll down until you reach Event Notification and EventsBridge.

 
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/0058ca0a-9098-401e-8585-fe741c4ab9ce)

 
- Click on Create Event Notification. Fill out the form. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/93d0f75c-038d-48c7-b64a-ba013618c04b)


- In Event Types section, select All objects create events. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/2252c21b-9c97-4949-9cd4-734f2ffec3fc)


- In the destination section, select SQS queue. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/0b7804c4-c0d0-4fa4-8602-b9ba8c17f894)

 
- Before clicking on save changes, we must create a SQS first. 


### Step 3: Create SQS first

- Click on Create queue to start the process.

 
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/64a3ce9b-81a6-4b06-96b4-9f3202734dd4)


- Fill out the form and select everything by default. Click on create queue.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/ca602fb1-a8df-4a49-ae02-372cadd1de05)


### Step 4: Change Access Policy

- Scroll down and click on Access policy.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/98419fca-16f8-4f7b-afd2-f3981bc2134e)

 
- It's time to change the accesss policy Permissions. At your right side, click edit then click on Policy generator.

 
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/6005dfc7-16ca-412e-a6a8-3427fb9713ef)


- Add a star * to Principal. 

- Select Actions "Send Messages".

- Now copy the ARN from the the template policy and paste it in the generator. 

- Click on Add statement. Then click on Generate Policy.
 
- Copy the generated policy and paste it in our Event Notification. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/30c126f0-e9cc-4c63-af92-c41824ab149c)

 
- Click on Update policy, and click on save the SQS. 

- Go back to the Event Notification page. Select the SQS in the dropdown button. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/865fff88-9c1e-4fc2-b892-75a528a8b74d)


- Click on Save changes to create your S3 Event Notification.

- As you see, your Event notification attached to SQS is created. 


### Step 4: Test Event Notification

- Go back to the SQS you created and click on Send and receive message.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/617805b6-0a24-4fc8-a129-c03d5a586885)

 
- Scroll down to receive messages and click on poll for messages.

 
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/cd822a39-d14c-4bfa-94ad-7a6ca1031ae0)


- You will see the message . Click on it.
 

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/9251103f-081a-48f7-9208-ea635de9f0e8)

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/b04cd156-3122-477e-afb0-759cc5abbf4a)
 

- As you can see, S3 Event notification has been created successfully.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/10abde94-b727-4711-8096-84c031a9ab3c)

