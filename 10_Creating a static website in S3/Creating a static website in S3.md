# Creating a static website in S3

Welcome to this new project. I will provide you a step by step guide to configure a static website on S3.

### Background

A static website is a website with individual webpages include static content. They might also contain client-side scripts. On the other hand, a dynamic website relies on server-side processing, including server-side scripts, such as PHP, JSP, or ASP.NET.

Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

### Prerequisite

For this project, you need an AWS account. Set up a Free-Tier account www.aws.amazon.com/free

### Project Outline

Configure a static website on Amazon S3.


#### First, create a S3 bucket

If you don’t know how to create a bucket, check my article (how to create a S3 bucket).


#### Second, enable static website hosting

•	Sign in to the AWS Management Console and open S3 console.

•	In the Buckets list, choose the name of the bucket that you created and enable static website hosting.

•	Select Properties. Under Static website hosting, select Edit.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/f82c51ac-3c1d-4425-ad23-edfe5d1087bf)

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/f9b35322-3b28-490e-857d-4d4a128f2d10)
 
•	Select Use this bucket to host a website.

•	Under Static website hosting, choose Enable.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/47fa1123-b5c7-4a00-a2bf-6d12e056454f)
 
•	In Index document, enter the file name of the index document, typically index.html.

•	In Error document, enter the custom error document file name.

•	Skip all the optional choice for now. Then, Select Save changes.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/8f72bd5b-ca83-48b8-a5a8-a91d046e4f82)
 
•	Under Static website hosting, note the Endpoint. In my case, the endpoint is http://djnewbucket.s3-website-us-east-1.amazonaws.com.
 
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/63e7c15c-6e67-41a4-94ec-8c158efa943b)


#### Third, edit Block Public Access settings

•	Back to S3 in the console

•	Select the name of the bucket that you have configured as a static website.

•	Select Permissions.

•	Under Block public access (bucket settings), choose Edit.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/9fef7fb2-bbd5-4af1-abeb-aefce38c46fa)
 
•	Clear Block all public access, and choose Save changes. Confirm.
 
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/a0ecb919-4b1a-40e2-854b-ba2baa3b9a50)


#### Fourth, add a bucket policy that makes your bucket content publicly available

•	Under Buckets, select the name of your bucket.

•	Select Permissions.

•	Under Bucket Policy, select Edit.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/7e7a2265-c85e-4ff3-a09d-cc8e8dd0d618)
 
To grant public read access for your website, copy the following bucket policy, and paste it in the Bucket policy editor.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/826836ed-0400-4124-a0a3-136f686da59b)
 
•	Update the Resource to your bucket name.

Cheat Sheet: In the preceding example bucket policy, Bucket-Name is a placeholder for the bucket name. To use this bucket policy with your own bucket, you must update this name to match your bucket name.

•	Select Save changes. A message appears indicating that the bucket policy has been successfully added.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/196207f7-8634-4591-9cf1-5542db5e8fec)
 
#### Fifth, Configure an index document.

Now it’s the time to create an index file. If you don’t know how to create an index file, use this one below:
 
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/25fc0342-c5fe-4786-ac65-30d38ba76d62)

•	Save the index file locally.

Cheat Sheet: the index document file name must exactly match the index document name that you enter in the Static website hosting dialog box.

•	In the Buckets list, choose the name of the bucket that you want to use to host a static website.

•	Enable static website hosting for your bucket, and enter the exact name of your index document (for example, index.html). For more information, see Enabling website hosting.

•	After enabling static website hosting, upload the index document to your bucket, do one of the following: drag and drop the index file into the console bucket listing, or select Upload, and follow the prompts to choose and upload the index file.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/6964e042-af70-41e3-a908-f53f5fb5e241)

 
#### Sixth, configure an error document.

•	Create an error document error.htmland save the error document file locally. The error document name is case sensitive and must exactly match the name that you enter when you enable static website hosting.

•	Back to AWS Management Console and open S3.

•	In the Buckets list, select the name of the bucket that you want to use to host a static website.

•	Verify that static website hosting for your bucket is still enable. If no, follow this instructions Enabling website hosting.

•	Now upload the error document to your bucket.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/50f27c15-873e-4260-a73e-5a21af675efb)

 
#### Finally, test your website endpoint

•	Under Buckets, select the name of your bucket. Select Properties.

•	At the bottom of the page, under Static website hosting, select Bucket website endpoint.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/b0143b47-973e-4c3c-b8d8-81dca302a072)
 
•	Your index document opens in a separate browser window.

Cheat Sheet: Amazon S3 does not support HTTPS access to the website. If you want to use HTTPS, you can use Amazon CloudFront to serve a static website hosted on Amazon S3.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/eb7d666c-9eaf-4690-a5bf-dd2fe852dc77)
 

Voilà! You now have a website hosted on Amazon S3. This website is available at the AWS S3 website endpoint.

Thank you for reading and/or following along! Please stay tuned for all my upcoming projects, and feel free to check out the rest of my tutorials.

