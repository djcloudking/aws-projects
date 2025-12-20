# Architecture Overview

## Network Layout
- VPC CIDR: 10.0.0.0/16
- Public Subnet: 10.0.1.0/24
- Private Subnet: 10.0.2.0/24
- Isolated Subnet: 10.0.3.0/24

## Routing
- Public subnet routes 0.0.0.0/0 to Internet Gateway
- Private subnet has no direct internet access
- Isolated subnet has no external routes

## Security
- Security Groups control instance-level access
- Network ACLs left default to avoid unintended blocking

## Design Intent
This layout reflects common enterprise environments where:
- Only specific resources are internet-facing
- Backend systems remain private
- Misconfiguration can easily cause access issues
