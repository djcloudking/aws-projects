# Deploy NodeJS app on EC2

In this short tutorial, I'll deploy a NodeJS app and show you how to create a AWS EC2 instance, SSH into the instance, install NodeJS and NPM, install Git, clone the repository from GitHub, install all the required dependencies, run the application and access the application in browser. 

Let's begin:

### Create a AWS EC2 instance

Click on [the link](https://github.com/djcloudking/aws-skills-challenges/tree/main/06_Compute%20(EC2)) to learn how to create a AWS EC2 instance. 


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/df3f207d-09ac-4b0c-806e-7fea3501affa)


### SSH into the instance

Here a reminder about how to SSH into an EC2 instance. Click [here](https://github.com/djcloudking/aws-skills-challenges/blob/main/11_Connect%20to%20EC2%20Instances%20with%20SSH%20and%20RDP/How%20to%20troubleshoot%20EC2%20instances.md).


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/49c35539-1627-48d6-b6f2-d3d23a7e4607)


After doing SSH into the EC2 instance you need to change the user to the super user by using the command : ***sudo su*** , so that you won’t have any user permission issues.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/f51d4793-c3b2-489d-a693-d8875d49a706)


## Install NodeJS and NPM using nvm

- Install nvm (node version manager) by entering the following at the command line: ***curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/6827f5f6-f5cc-4cd8-903c-7a3b88bd8385)


- Activate nvm by using: ***. ~/.nvm/nvm.sh***

- By using nvm you have to install Node.js: ***nvm install node***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/158734f9-8fd8-40f6-8c63-8fe15a62cc40)


- Verify the nvm and Node.js installation by typing in the terminal: ***nvm --version*** then ***node -v***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/05784df8-10f8-4d3e-80d1-3b411b0a4bf0)


## Install Git

- Install Git so that you can clone the repository containing the Node.JS app

- First update all software packages: ***yum update -y***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/9d209111-c294-4c4a-80fa-fc575c1bb580)


- Then, install git: ***yum install git -y***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/c317ff01-83db-4091-9b01-cf9cd18975ea)


- verify if git was installed correctly: ***git --version***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/968c52c6-f874-4750-a797-d7c82fd83a68)


## Clone the repository from GitHub

- Clone the repo: ***git clone https://github.com/rajani103/nodejs-on-ec2.git***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/4afc8969-2b5c-40c4-be33-82615dd26669)


- List the contents of the repo: ***ls -ltr***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/068b58a0-2c9d-44b3-a65f-0c8676299a2b)


- Verify the folders and sub-folders.


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/3f9cd785-cb32-4780-b053-6dec8c441772)


## Install all the required dependencies

- Install the dependencies: ***npm install***


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/006c3440-5a55-4417-bdf5-68a4cfa044ea)


### Run the application

- It's time to run the app: ***node index.js***


### Access the application in browser

- Now you should be able to see the app using the public IP of the machine or the public DNS of the machine


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/c25ffdb2-c1f1-4765-b662-64296b8fde07)


![image](https://github.com/djcloudking/aws-skills-challenges/assets/122766532/0241606e-14f4-4671-9000-df055cf1c066)


Congrats, by following these steps, you just deployed a NodeJS app on AWS EC2. 
