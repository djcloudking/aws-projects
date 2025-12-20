# Runbook – VPC Connectivity Validation

## Purpose
Ensure EC2 instances in public subnets are reachable after deployment.

## Pre-Checks
- Confirm VPC and subnet CIDRs
- Validate route table associations

## Standard Validation Steps
1. Launch test EC2 instance
2. Verify public IP assignment
3. Check Security Group inbound rules
4. Confirm route to Internet Gateway
5. Test SSH connectivity

## Rollback
- Reassociate subnet with last known good route table
- Remove recent routing changes

## Escalation
- Escalate to network or cloud platform team
- Provide subnet ID, route table ID, and security group ID
