# Deploy NodeJS app on EC2

In this short tutorial, I'll deploy a NodeJS app and show you how to create a AWS EC2 instance, SSH into the instance, install NodeJS and NPM, install Git, clone the repository from GitHub, install all the required dependencies, run the application and access the application in browser. 

Let's begin:

### Create a AWS EC2 instance

Click on [the link](https://github.com/djcloudking/aws-skills-challenges/tree/main/06_Compute%20(EC2)) to learn how to create a AWS EC2 instance. 


### SSH into the instance

Here a reminder about how to SSH into an EC2 instance. Click [here](https://github.com/djcloudking/aws-skills-challenges/blob/main/11_Connect%20to%20EC2%20Instances%20with%20SSH%20and%20RDP/How%20to%20troubleshoot%20EC2%20instances.md).

After doing SSH into the EC2 instance you need to change the user to the super user by using the command : ***sudo su*** , so that you won’t have any user permission issues.


## Install NodeJS and NPM using nvm

- Install nvm (node version manager) by entering the following at the command line: ***curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash***

- Activate nvm by using: ***. ~/.nvm/nvm.sh***

- By using nvm you have to install Node.js: ***nvm install node***

- Verify the nvm and Node.js installation by typing in the terminal: ***nvm --version*** then ***node -v***


## Install Git

- Install Git so that you can clone the repository containing the Node.JS app

- First update all software packages: ***yum update -y***

- Then, install git: ***yum install git -y***

- verify if git was installed correctly: ***git --version***


## Clone the repository from GitHub

- Clone the repo: ***git clone https://github.com/rajani103/nodejs-on-ec2.git***

- Liste the contents of the repo: ***ls -ltr***

- Verify the folders and sub-folders.


## Install all the required dependencies

- Install the dependencies: ***npm install***


### Run the application

- It's time to run the app: ***node index.js***


### Access the application in browser

- Now you should be able to see the app using the public IP of the machine or the public DNS of the machine

