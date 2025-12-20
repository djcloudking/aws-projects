# Incident: EC2 Instance Unreachable After Deployment

## Summary
An EC2 instance launched in a public subnet was unreachable via SSH
despite showing a healthy "running" state in AWS.

## Severity
SEV-2

## Impact
- Engineering team could not access the instance
- Delayed application deployment
- No customer-facing outage

## Detection
- SSH connection timed out
- Instance passed EC2 system and instance checks
- CloudWatch metrics showed normal CPU and network activity

## Root Cause
The subnet route table did not include a default route (0.0.0.0/0)
to the Internet Gateway.

## Resolution
- Identified route table misconfiguration
- Added default route to Internet Gateway
- Verified SSH access from approved IP range

## Prevention / Follow-Up
- Added route table validation to deployment checklist
- Documented known failure mode in runbook
- Recommended post-deployment connectivity tests

## Lessons Learned
Instance health does not guarantee network reachability.
Routing must always be validated at the subnet level.
