# VPC

## Background
Amazon VPC lets you provision a logically isolated section of the Amazon Web Services (AWS) cloud where you can launch AWS resources in a virtual network that you define.

With VPC you control your virtual networking environment, including selection of your own IP address ranges, creation of subnets, and configuration of route tables and network gateways.

## Prerequisite
For this project, you need an AWS account. Set up a Free-Tier account www.aws.amazon.com/free.

## Project Outline

Build a VPC with 3 subnets named “Web”, “App”, and “Data”. The “Web” subnet should contain half the available IPV4 addresses while the other two contain one quarter each. Each subnet should be in a separate Availability Zone within the same AWS region. VPC CIDR: 10.1.1.0/24.

Now let’s have fun

- Log in to your AWS console, select Us-east-1 (N. Virginia) as your region and go to the VPC dashboard.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/4eb206c1-692d-4afa-9e82-b9d8e49cd850)

- Then click on “Create VPC’.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/049b1447-2faa-4ffd-be98-b70c2e6fca42)

- Select VPC and more for resources to create.

- Leave “auto-generate” checked. You can change the name or leave it as default.

Cheat Sheet: the names that you specify for the VPC and the other VPC resources are used to create Name tags. If you use the name tag auto-generation feature in the console, the tag values have the format name-resource.

- For IPv4 CIDR block, Enter “10.1.1.0/24” as the CIDR block for your VPC. 

- For IPv6 CIDR block, check “no IPv6 CIDR block”.

- For Tenancy, Choose the default option “default”.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/1f18f648-34bb-4fa6-9db2-a113a0c5d220)

Cheat Sheet: A VPC must have an IPv4 address range. To support IPv6 traffic, you can select IPv6 CIDR block, Amazon-provided IPv6 CIDR block.

- For availability zone, choose 3.

- For public/private subnet, click on zero (0). You will create subnets associate them to this vpc later in the process.

- For everything else (or the following options), leave the “default” version.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/9c532cc8-14ba-4608-8366-451064582966)

- Then click on “Create VPC”.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/a323c09d-3096-48a9-8685-9f4f5bb0dfd9)
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/d4ab2146-b0d2-46a3-92f8-2d665a6f2f6b)

After your VPC is created, click on “Create Subnet” on the left side of your dashboard to create your first subnet named “Web”.

Click on “create subnet” again and follow the wizard.

Select the VPC ID you just created a moment ago.

- In subnet settings, enter the “Web” as the name of your subnet. Then, choose the VPC you just created from the dropdown menu. Choose an available Availability Zone from the dropdown menu. Now, enter “10.1.1.0/25” as the CIDR block for your Web subnet. Finally, click on “Create” to create your Web subnet.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/10f229cb-6775-494a-bdc5-94529d28168f)

- Repeat the same steps to create your second subnet named “App”. In subnet settings, enter the “Web” as the name of your subnet. Then, choose the VPC you just created from the dropdown menu. Choose a different Availability Zone from the one you selected for your App subnet. Enter “10.1.1.128/26” as the CIDR block for your App subnet. Finally, click on “Create” to create your App subnet.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/14d4c6a8-2ed1-4c9d-a394-fc0e752e60dd)

- Repeat the same steps to create your third subnet named “Data”. In subnet settings, enter the “Data” as the name of your subnet. Then, choose the VPC you just created from the dropdown menu. Choose a different Availability Zone from the ones you selected for your Web and App subnets. Now, enter “10.1.1.192/26” as the CIDR block for your Data subnet. Finally, click on “Create” to create your Data subnet.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/882fd740-e4ca-43ac-9865-0106305d3fb0)


Your VPC with 3 subnets named “Web”, “App”, and “Data” is ready to use.

![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/5e32e535-9e0a-44fd-83e7-6b8243de5b3d)
![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/31896077-f2f3-4c15-82bd-19166bb4bb00)


Cheat Sheet: Each subnet must reside entirely within one Availability Zone and cannot span zones.

Voilà! you have built a VPC with 3 subnets (and IPV4 addresses, separate Availability Zones within the same AWS region, and VPC CIDR: 10.1.1.0/24).

Thank you for reading and/or following along! Please stay tuned for all my upcoming projects, and feel free to check out the rest of my articles.
