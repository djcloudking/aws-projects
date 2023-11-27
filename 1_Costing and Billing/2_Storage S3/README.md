Welcome to another AWS Skills challenge. This mini-project is divided into two parts: part 1 includes how to create your first bucket, part 2 includes uploading an object to your bucket. This is the perfect challenge to get familiar with AWS S3.

Background
Amazon S3 is object storage service built to store and retrieve any amount of data from anywhere. S3 is a simple storage service that offers industry leading durability, availability, performance, security, and virtually unlimited scalability at very low costs.

Amazon S3 provides a simple web service interface that you can use to store and retrieve any amount of data, at any time, from anywhere. Using this service, you can easily build applications that make use of cloud native storage.

Prerequisite
For this mini-project, you need an AWS account. Set up a Free-Tier account www.aws.amazon.com/free

Project Outline
Create a Private S3 bucket and copy a file into it using the AWS console or AWS CLI.

Now let’s have fun “practicing”.

Part 1: Create your first bucket
After creating your free tier AWS account, sign in to the AWS Management Console.

Search S3 and open the Amazon S3 console.
In the left navigation pane, choose Buckets or choose Create bucket (orange rectangle) at your right.

The Create bucket page opens. Fill out the form (Bucket name, AWS Region, etc.). See bucket naming convention.

Cheat Sheet: For Region, choose the AWS Region where you want the bucket to reside. To minimize latency and costs and address regulatory requirements, choose a Region close to you.

From there you can leave everything checked by default. If you want to make changes and choose what you want to apply, make sure to read this for more.

Last, choose Create bucket. You have created your first bucket successfully.

Part 2: Upload a file into the file using the AWS console or AWS CLI.
After creating a bucket in Amazon S3, it’s time to upload an object to the bucket. An object can be any kind of file (a text file, a photo, a video).

Go to the Buckets list, and choose the name of the bucket that you created to upload your object to.
On the Objects tab for your bucket, choose Upload.
Under Files and folders, choose Add files.

Select a file to upload, and select Open. Then select Upload.

You’ve successfully uploaded an object to your bucket.


Voilà! You have created a S3 bucket and uploaded an object to it using AWS console.

Thank you for reading and/or following along! Please stay tuned for the 3rd challenge (Networking VPC) and all my upcoming projects, and feel free to check out the rest of my articles.