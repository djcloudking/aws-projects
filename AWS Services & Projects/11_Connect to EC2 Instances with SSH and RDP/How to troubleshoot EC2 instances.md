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

- In the new interface, click on **Launch instances**

- Fill out the form by adding the name of your EC2. 


### Step 2: Create a keypair

- In the form, you have 2 options: use an existing keypair or create a new keypair. Click on **Create new keypair**.

Cheat Sheat: When creating a new key pair, select an easily memorable name. Choose a RSA key pair type and opt for the .pem key file format.

- Download your key onto your local computer. Be aware of where you save the .pem file and how you identify the key later when connecting to the instance.


### Step 3: Assign Security Groups and Ports

- (Still in the same form) create a security group or select an existing one. 

- Select "Allow SSH traffic from" and "My IP". 

- Now launch your instance.


### Step 4: Verify the SSH connection

- Navigate back to EC2 dashboard.

- Click on “Instances” tab located on the left-hand side. 

- Locate your instance within the list, and then click on the “Instance ID”. 

- Go to SSH Client tab, and read the instructions. AWS has provided the command to connect to EC2 via SSH, which you can copy and run in the terminal.

- Locate and click on the “Connect” button to proceed. 

- When the next page loads, it should automatically open into the “SSH client” tab, providing all the necessary information to connect to your instance.

- Now, let’s open our command line from your local computer. In this case, make sure your AWS account has been configured before. 

- Locate your .pem file before running any commands. Use the **cd** command. 

Cheat Sheet: *Once you’re in the correct directory, you copy the command from the “Connect” tab in the AWS console and paste it into your terminal. Then, execute the command. If this is your first time connecting to the instance with this particular IP address, it will prompt you to confirm the connection. Type “yes” into the command line and press Enter to proceed.*

- Run "whoami" to double check if we are now connected.


**We’ve deployed an EC2 instance and connected to it with SSH.**


## Stage 2: Connecting to EC2 instances with RDP

Let's replicate the same steps for RDP connection.


### Step 1: Log in to EC2 dashboard

- Go back to your EC2 dasboard, and create an instance.

- Fill out the form by adding a name. Select Windows as AMI image. Then create a new keypair and a security group.


### Step 2: Create a keypair

- Do the same process as before. Remember to select an easily memorable name, a RSA key pair type and opt for the .pem key file format.


### Step 3: Assign Security Groups and Ports

- (Still in the same form) create a security group or select an existing one. 

- Select "Allow SSH traffic from" and "My IP". 

- Now launch your instance.


### Step 4: Verify the RDP connection

- Navigate back to EC2 dashboard.

- Click on “Instances” tab located on the left-hand side. 

- Locate your instance within the list, and then click on the “Instance ID”. 

Cheat Sheet: *There’s a difference in the “Connect” page compared to the Linux server.*

- Click on the “Download remote desktop” file to install Windows RDP onto your PC.

- Click on the “Get password” icon bolded in dark grey. Input your .pem file, which allows you to retrieve the password for your RDP session. 

- Open your RDP application and input the generated password associated with the “Administrator” username.


**Voila! We’ve deployed an EC2 instance and connected to it with RDP.**