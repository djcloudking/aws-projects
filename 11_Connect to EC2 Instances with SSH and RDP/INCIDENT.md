### Incident

**Incident Title**: EC2 Instance Unreachable via SSH
**Service**: EC2
**Severity**: SEV-2
**Duration**: 27 minutes

**Summary**
An EC2 instance became unreachable via SSH, impacting administrative access during a routine maintenance window.

**Impact**
- Engineers unable to access the instance
- No customer-facing downtime
- Delayed patching activity

**Detection**
- SSH timeout reported by engineer
- Instance showed running in EC2 console
- CloudWatch showed normal CPU and network

**Root Cause**
Security Group inbound rule for port 22 was removed during a configuration update.

**Resolution**
- Identified missing inbound SSH rule
- Restored rule allowing port 22 from approved IP range
- Confirmed connectivity via SSH

**Prevention / Follow-Up**
- Added validation step to runbook
- Recommended Security Group change monitoring
- Documented known failure mode

**Lessons Learned**
Running state does not guarantee reachability. Network controls must be validated after any change.