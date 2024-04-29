# Using AWS CodePipeline create your first CI/CD Pipeline


In this tutorial, I will create a simple pipeline between S3 buckets using AWS CodePipeline.

 
## Background

AWS CodePipeline streamlines the management of continuous delivery, providing automated release pipelines to swiftly and securely update both applications and infrastructure.

You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.


## Project Outline

Create a simple pipeline between S3 buckets using AWS CodePipeline.


## Prerequisite

- Access to AWS account.

- Create a static website contents


## Let’s have fun.


### Step 1- Create a S3 bucket as the source repository

•	Log in to your AWS account.

•	Go to AWS S3 dashboard.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/e21b5b74-d0cd-46ab-861b-2fa719d825f8)

 
•	Choose Create bucket.

•	In the next window, AWS Region is selected automatically.

•	Leave Bucket Type as General purpose by default.

•	In Bucket name, enter a name for your bucket (mine is demo-website-source).


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/b3d085bb-5c6f-433e-91b0-812ec1cb98e6)

 
*Cheat Sheet: Because all bucket names in Amazon S3 must be unique, use one of your own, not the name shown in the example. You can change the example name just by adding the date to it. Make a note of this name because you need it for the rest of this tutorial.*

•	Scroll down in the configuration, and don’t make any changes until you reach versioning properties.

•	At the Versioning section, choose Enable versioning.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/82529dc6-e3aa-4baa-9d83-3d67871d3964)

 
•	Scroll down and leave everything as default. Then click Create bucket.


## Step 2- Create another S3 bucket as the production repository

•	Repeat the same process as above.

•	In Bucket name, enter a name for your bucket (mine is demo-website-prod).

•	In Object Ownership, select ACL enabled.

•	In the bucket configuration, uncheck Block all public access this time.

•	Leave everything else by default.

Congratulations you’ve created two S3 bucket but the tutorial is not completed yet.

•	Now, go to list of S3 buckets. Click on the production bucket demo-website-production.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/25479ae0-b8d8-4f2d-b379-a8300a9bbf94)

 
•	Click Property, and scroll to static website hosting. Click Edit.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/66729a23-e635-4bb1-b10c-d56c4401e1b3)

 
•	Select Enable for Static website hosting. Select Host a static website for Hosting type.

•	Add index.html and error.html for documents.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/ffa48592-b1bf-490f-94cd-59d7366a1e56)

 
•	Click Save changes.

•	Click on the link at the bottom of the window. You should see this error message because we have not upload any contents yet.
 

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/fa0efc78-0bf8-4424-bf0f-b5260da330f5)


## Step 3- Add contents to the production bucket

•	Locate your website contents on your personal computer.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/6d9c85c6-339d-497e-a231-ab66b282fb77)

 
•	Create a zip package and name it demo-website.zip.

•	Go back to the S3 source bucket to upload website contents.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/22fe62d9-14b4-40be-bc6a-05f5e827a3c2)

 
•	After uploading successfully, it’s time to create our pipeline.


## Step 4- Create a new pipeline via AWS Codepipeline

•	Go to AWS Codepipeline dashboard.
 
•	Choose Create pipeline.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/a25a2b9f-313b-4add-b34d-2d1f045e13d5)


•	In pipeline settings, add a name. Select pipeline type, service role, role name.

•	Check Allow AWS CodePipeline to create a service role so it can be used with this new pipeline.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/75a06058-1c10-4d07-8c1f-9b2e3805b8d1)

 
•	In advanced settings, select default location for artifact store, and Default AWS managed key for Encryption key.


 ![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/5b934e47-2872-49cc-9d5e-62c4fe7e29aa)


•	Click Next.

•	In the source stage, add the source provider as Amazon S3; the bucket as demo-website-source; and S3 boject key as demo-website.zip.

•	Choose Amazon CloudWatch Events for detection options.

•	Click Next.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/7153a10b-173d-49ff-b222-ff06e7ff2819)

 
•	Skip the build stage. We don’t need it in this short tutorial.

•	In the Deploy stage, Choose Amazon S3 as Deploy provider, same region. Add demo-website-prod as Bucket.

•	Select Extract file before deploy.

•	In additional configuration, select Public-read for canned-ACL.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/3e6e6b79-1759-4dd0-9522-f8ca55d71b26)

 
•	Click Next, and Create pipeline.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/2174c1c4-cbc4-47ad-88a2-e8ae421e0994)

 
Congratulations you’ve created your first pipeline using AWS Codepipeline.


## Step 5- Verify

•	Go back to the static website hosting in demo-website-prod S3 bucket.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/97b26843-093c-47c0-a2d6-21b6183cf0e9)

 
•	Click on the URL at the bottom of the page.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/99049315-5650-48ee-a58a-52067d1ebbd9)

 
Voilà! You now know how to create a simple pipeline between S3 buckets using AWS CodePipeline.

