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
 
•	Choose Create bucket.

•	In the next window, AWS Region is selected automatically.

•	Leave Bucket Type as General purpose by default.

•	In Bucket name, enter a name for your bucket (mine is demo-website-source).
 
*Cheat Sheet: Because all bucket names in Amazon S3 must be unique, use one of your own, not the name shown in the example. You can change the example name just by adding the date to it. Make a note of this name because you need it for the rest of this tutorial.*

•	Scroll down in the configuration, and don’t make any changes until you reach versioning properties.

•	At the Versioning section, choose Enable versioning.
 
•	Scroll down and leave everything as default. Then click Create bucket.


## Step 2- Create another S3 bucket as the production repository

•	Repeat the same process as above.

•	In Bucket name, enter a name for your bucket (mine is demo-website-prod).

•	In Object Ownership, select ACL enabled.

•	In the bucket configuration, uncheck Block all public access this time.

•	Leave everything else by default.

Congratulations you’ve created two S3 bucket but the tutorial is not completed yet.

•	Now, go to list of S3 buckets. Click on the production bucket demo-website-production.
 
•	Click Property, and scroll to static website hosting. Click Edit.
 
•	Select Enable for Static website hosting. Select Host a static website for Hosting type.

•	Add index.html and error.html for documents.
 
•	Click Save changes.

•	Click on the link at the bottom of the window. You should see this error message because we have not upload any contents yet.
 
## Step 3- Add contents to the production bucket

•	Locate your website contents on your personal computer.
 
•	Create a zip package and name it demo-website.zip.

•	Go back to the S3 source bucket to upload website contents.
 
•	After uploading successfully, it’s time to create our pipeline.

## Step 4- Create a new pipeline via AWS Codepipeline

•	Go to AWS Codepipeline dashboard.
 
•	Choose Create pipeline.

•	In pipeline settings, add a name. Select pipeline type, service role, role name.

•	Check Allow AWS CodePipeline to create a service role so it can be used with this new pipeline.
 
•	In advanced settings, select default location for artifact store, and Default AWS managed key for Encryption key.
 
•	Click Next.

•	In the source stage, add the source provider as Amazon S3; the bucket as demo-website-source; and S3 boject key as demo-website.zip.

•	Choose Amazon CloudWatch Events for detection options.

•	Click Next.
 
•	Skip the build stage. We don’t need it in this short tutorial.

•	In the Deploy stage, Choose Amazon S3 as Deploy provider, same region. Add demo-website-prod as Bucket.

•	Select Extract file before deploy.

•	In additional configuration, select Public-read for canned-ACL.
 
•	Click Next, and Create pipeline.
 
Congratulations you’ve created your first pipeline using AWS Codepipeline.

*Step 5- Verify*

•	Go back to the static website hosting in demo-website-prod S3 bucket.
 
•	Click on the URL at the bottom of the page.
 
Voilà! You now know how to create a simple pipeline between S3 buckets using AWS CodePipeline.

