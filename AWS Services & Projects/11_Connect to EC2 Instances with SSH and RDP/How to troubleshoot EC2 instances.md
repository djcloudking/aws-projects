# Connect to EC2 Instances with SSH and RDP

This brief tutorial demonstrates how to establish connections to an EC2 instance using SSH and RDP, particularly useful for troubleshooting purposes.


## Prerequisite

For this project, you need:

- an AWS account. Set up a Free-Tier account www.aws.amazon.com/free

- the private key file (.pem or .ppk) associated with the instance.


## Project Outline

Establish connections to an EC2 instance using SSH and RDP.


## Stage 1: Connecting to EC2 instances via SSH


### Step 1: Log in to EC2 dashboard

- On the left-hand side of your EC2 dasboard, click on **Instances**


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/5a24f791-16b8-4ce5-aa24-5c6a39ba6a7b)


- In the new interface, click on **Launch instances**


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/47d8636d-869e-417e-acf0-4b6d1f5fe114)


- Fill out the form by adding the name of your EC2. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/692841d3-cf02-4286-8726-ee66a7ec8fbb)


### Step 2: Create a keypair

- In the form, you have 2 options: use an existing keypair or create a new keypair. Click on **Create new keypair**.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/e4e20279-736e-45de-863e-d97e9ec3adde)


*Cheat Sheat: When creating a new key pair, select an easily memorable name. Choose a RSA key pair type and opt for the .pem key file format.*

- Download your key onto your local computer. Be aware of where you save the .pem file and how you identify the key later when connecting to the instance.


### Step 3: Assign Security Groups and Ports

- (Still in the same form) create a security group or select an existing one. 

- Select "Allow SSH traffic from" and "My IP".


<img width="446" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/615cbe99-d6f6-467e-a452-28cc8a075945">


- Now launch your instance.


### Step 4: Verify the SSH connection

- Navigate back to EC2 dashboard.

- Click on “Instances” tab located on the left-hand side. 

- Locate your instance within the list, and then click on the “Instance ID”. 

- Go to SSH Client tab, and read the instructions. AWS has provided the command to connect to EC2 via SSH, which you can copy and run in the terminal.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/e71dcf7d-6e07-4d6a-977d-f6405e9122d7)


- Locate and click on the “Connect” button to proceed. 

- When the next page loads, it should automatically open into the “SSH client” tab, providing all the necessary information to connect to your instance.

- Now, let’s open our command line from your local computer. In this case, make sure your AWS account has been configured before. 

- Locate your .pem file before running any commands. Use the **cd** command. 

Cheat Sheet: *Once you’re in the correct directory, you copy the command from the “Connect” tab in the AWS console and paste it into your terminal. Then, execute the command. If this is your first time connecting to the instance with this particular IP address, it will prompt you to confirm the connection. Type “yes” into the command line and press Enter to proceed.*


<img width="449" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/61c249d6-d37c-4568-b2cf-b9409d3e3633">


- Run "whoami" to double check if we are now connected.


<img width="394" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/72f4c038-c88b-462b-9dbd-83bd233127e4">


**We’ve deployed an EC2 instance and connected to it with SSH.**


## Stage 2: Connecting to EC2 instances with RDP

Let's replicate the same steps for RDP connection.


### Step 1: Log in to EC2 dashboard

- Go back to your EC2 dasboard, and create an instance.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/cbcb62c8-70fd-4b3c-b549-730c3d33f478)


- Fill out the form by adding a name. Select Windows as AMI image. Then create a new keypair and a security group.


<img width="451" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/18444823-baca-4ebe-a9a6-b89449fe455c">


### Step 2: Create a keypair

- Do the same process as before. Remember to select an easily memorable name, a RSA key pair type and opt for the .pem key file format.


### Step 3: Assign Security Groups and Ports

- (Still in the same form) create a security group or select an existing one. 

- Select "Allow SSH traffic from" and "My IP". 

- Now launch your instance.


### Step 4: Verify the RDP connection

- Navigate back to EC2 dashboard.

- Click on “Instances” tab located on the left-hand side. 

- Locate your instance within the list, and then click on the “Instance ID”. Then click on RDP client. 

<img width="455" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/7bb6e2c1-b6d4-4f7d-b7a7-d5d2bca2291a">


Cheat Sheet: *There’s a difference in the “Connect” page compared to the Linux server.*

- Click on the “Download remote desktop” file to install Windows RDP onto your PC. Then click on Connect.


<img width="395" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/9afa4150-80a6-4008-aa27-bd4b6edd89c5">


- Click on the “Get password” icon bolded in dark grey. Input your .pem file, which allows you to retrieve the password for your RDP session. 

- Open your RDP application and input the generated password associated with the “Administrator” username.


<img width="341" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/df7edbb9-04d9-42c7-8f4d-e7b0d941852a">


- Click "Yes".


<img width="281" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/150e3f59-45dc-4a33-84a1-349c1e419da9">


<img width="453" alt="image" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/afd7c6fb-90fc-4d9e-8069-d1a8f18cb02d">


**Voila! We’ve deployed an EC2 instance and connected to it with RDP.**
