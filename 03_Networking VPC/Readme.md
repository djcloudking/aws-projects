# Networking – VPC Operations

## What Was Built
A custom AWS VPC with:
- 3 subnets (public, private, isolated)
- Internet Gateway
- Route tables
- Security Groups
- Network-level access controls

## Why This Exists (Operations Context)
VPC networking issues are a common root cause of production outages.
This project focuses on identifying and resolving connectivity failures
between instances, services, and the internet.

## AWS Services Used
- VPC
- Subnets
- Route Tables
- Internet Gateway
- Security Groups
- EC2

## Operational Risks Demonstrated
- Incorrect route table associations
- Missing or overly restrictive security group rules
- Public subnet misconfiguration
- Instances marked as "running" but unreachable

## How to Review This Folder
- Read `INCIDENT.md` to understand a real outage scenario
- Follow `TROUBLESHOOTING.md` for step-by-step diagnosis
- Use `RUNBOOK.md` for standard operating procedures
