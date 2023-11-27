# Costs and Billing

## Prerequisite:

For this mini-project, you need an AWS account. Set up a Free Tier account www.aws.amazon.com/free

## Project Outline

Costs and Billing: Create a recurring monthly Budget and Budget Alert. Name it: [name]_BUDGET. Set budget to $10.00, scope to All Services. Set a “90% of budget” alert to email to your email address.

## Introduction to Budget
A budget is necessary to track and take action on your costs and usage. By default, single accounts, the management account, and member accounts in an organization can create budgets.

When you create a budget, AWS Budgets provides a Cost Explorer graph to help you see your incurred costs and usage.

It’s possible to track against the following budgets:

- Cost
- Usage
- Savings Plans (Savings Plans utilization, Savings Plans coverage)
- Reservation (Reservation utilization, Reservation coverage).
  
For this exercise, we will focus on Cost budget.

## Now let’s have fun

- After creating your free tier AWS account, sign in to the AWS Management Console.

  <img width="941" alt="aws console 1" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/b660dfb4-5d66-4b95-8131-3306525cca19">


- Then open the AWS Cost Management console. In the navigation pane, choose Budgets.


  <img width="943" alt="aws console 2" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/33681daa-d72d-4e8d-8cb0-ba7b8334479b">


- At the top of the page, choose Create budget. Under Budget setup, choose between Use a template (simplified) and Customize (advanced).

Note: Customize (advanced) gives an option to customize the time period, the start month and specific amounts.

- Select Use a template (simplified). Scroll down and fill out the form.

  <img width="789" alt="AWS console 3" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/7a744397-6b9d-4040-a943-131471885d2f">


- Select Monthly cost budget (remember our goal, see project outline).
Add the budget name, the budgeted amount, the email recipient you want to notify when the threshold has exceeded.

Note: it’s possible to add several emails.

<img width="587" alt="aws console 4" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/5b1580db-de59-43a6-bde1-86b71f5957bf">


- Once again remember our goal. We must set a “90% of budget” alert.

Note: In order to be notified on the state of our budget, we can create up to 5 different alerts based on your budgeted amount.

<img width="557" alt="aws console 5" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/6db6f3c9-0ce1-4cad-b5cf-354ce5436ef3">


- Also, we have the option to attach actions that run whenever our alert threshold has been exceeded, such as stopping an EC2 instance from incurring any further costs.

- Verify everything has been created and filled out correctly. Then click create budget.

<img width="938" alt="aws console 6" src="https://github.com/djcloudking/aws-skills-challenges/assets/122766532/ec1a60cb-0344-48a9-8b4e-f77d05210a82">


Voila! Our recurring monthly Budget DJ_BUDGET and Budget Alert is set budget to $10.00, scoped to All Services. When a service reaches “90% of budget”, an alert will be sent to my email djkone2025@gmail.com. You’ve now developed an additional AWS skill.

Thank you for reading and/or following along! Please stay tuned for the 2nd challenge (Storage S3) and all my upcoming projects, and feel free to check out the rest of my articles at www.fahmacloud.com
