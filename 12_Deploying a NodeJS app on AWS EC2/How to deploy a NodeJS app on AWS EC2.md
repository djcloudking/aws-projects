# Deploying a NodeJS App on AWS EC2


## Objective

This short project aimed to establish a connection between a random user and EC2, a NodeJS app and outside communication. 

The primary focus was to  deploy an application on to EC2 and expose it to the outside world. 

This hands-on experience was designed to deepen understanding of EC2, IAM and outside application deployment strategies.


## Skills Learned

•	Advanced understanding of IAM User.
•	Proficiency in EC2 instances.
•	Ability to deploy an application on to EC2.
•	Enhanced knowledge of EC2 best practices.
•	Development of critical thinking and problem-solving skills in AWS services.

1. How to create a IAM USER and Login 
2. How to create EC2 Instance ? What are some of the good practices ?
3. How to access the EC2 Instance ?
4. Deploy an application on to AWS EC2 ?
5. Expose the application to outside world ?
6. Access the application deployed on AWS from your laptop.

# Tools Used

•	AWS IAM for logging purpose.

•	AWS EC2 for deploying server.

•	NodeJS for application architecture.


## Steps


### Step 1: Setting up environment locally

- Let me test locally (on my laptop directly) before deploying our app to AWS. For that reason, I am going to clone a repository containing NodeJS app from github. 

- Open your terminal and type git clone https://github.com/verma-kunal/AWS-Session.git

- Setup the following environment variables - (.env) file using the commands below:

DOMAIN= ""
PORT=3000
STATIC_DIR="./client"

PUBLISHABLE_KEY=""
SECRET_KEY=""

- Name Domain as "http://localhost:3000". For publishable key and secret key, I will use Stripe API key. If you don't know, Stripe is a payment gateway. So you can find the API key online easily. 

Cheat Sheet: Follow the steps below to reveal a secret API key for test mode for Stripe.

Before revealing a secret key in test mode, you must login to your stripe account. If you don't have one, create an account here: https://dashboard.stripe.com/test/apikeys 

1. In the Developers Dashboard, select the API keys tab.
2. In the Standard keys list, in the Secret key row, click Reveal test key.
3. Copy the key value by clicking it.
4. Save the key value.
5. Click Hide test key.

- Paste the keys in the env file. Save it. 

- Now, initialise and start the project. Type the follwing commands:
npm install
npm run start

- 

- 

### Step 2: Deploying application on to AWS EC2
