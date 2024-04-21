## Elastic Compute Cloud: AWS EC2


An EC2 instance is a virtual server in the AWS Cloud.

### Background

Amazon EC2 (Elastic Compute Cloud) is a web service provided by Amazon Web Services (AWS) that allows you to launch and manage virtual servers, known as EC2 instances, in the cloud. 

EC2 provides scalable computing capacity in the cloud, allowing you to quickly provision and configure virtual machines to meet your computing requirements.

EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change. 

EC2 changes the economics of computing by allowing you to pay only for capacity that you actually use.


### Prerequisite

For this project, you need an AWS account. Set up a Free-Tier account www.aws.amazon.com/free.

### Project Outline

Launch an Amazon Linux 2 EC2 Instance.

### Steps

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/374141a1-a7e4-4f27-9033-28a502622b27)

##### Cheat Sheet: 
Select a Region for the instance that meets your needs. This choice is important because some Amazon EC2 resources can be shared between Regions, while others can’t. For more information, see Resource locations.

2. From the Amazon EC2 console dashboard, choose Launch instance.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/6c5ae657-5a6c-4239-936d-dd8447a5742d)

3. Name your instance in “Name and tags” section.

4. Choose an AMI. Make sure you select a free tier if you don’t want to pay.

##### Cheat Sheet: 

Amazon Machine Image (AMI) is a configuration that contains the information required to create a new instance. For example, an AMI might contain the software required to act as a web server, such as Linux, Apache, and your website.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/acb0f935-9d0a-48bd-95a4-6b26c1ffd496)

5. Choose an instance type.

6. Create a new keypair or Select an existing Key Pair.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/677bba4d-b2ac-4c78-b0f5-04cbc79b8468)

6. Create a Security Group or Select an existing Security group.

7. Create a new VPC (and subnets) or Select an existing VPC (and subnets).

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/445433dd-cec6-4d6b-9e70-93a89b5e012e)

8. In Configure Storage and Advanced Details Sections, leave all configuration by default.

9. Click on “Launch instance”.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/8c2820c6-8d51-4fe3-9fa3-2920741499a3)

Voilà! You have launched an Amazon Linux 2 EC2 Instance! You can now use this function in your other AWS services or applications.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/940f67c3-b785-45d4-b0ec-d932651322a7)


