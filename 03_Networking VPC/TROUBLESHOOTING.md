# Troubleshooting Guide – VPC Connectivity Issues

## Step 1: Verify Instance State
- Confirm instance is running
- Check EC2 system and instance status checks

## Step 2: Validate Security Group Rules
- Inbound SSH (22) allowed from approved IP
- Outbound traffic allowed

## Step 3: Check Subnet Route Table
- Confirm subnet association
- Verify 0.0.0.0/0 route exists
- Confirm route target is Internet Gateway

## Step 4: Validate Internet Gateway
- IGW attached to correct VPC

## Step 5: Confirm Public IP
- Instance has public IPv4 address
- Or Elastic IP attached

## Common Failure Modes
- Subnet associated with wrong route table
- Missing default route
- Security Group allows traffic but routing blocks it
