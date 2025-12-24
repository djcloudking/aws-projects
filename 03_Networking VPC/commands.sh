# Check route tables
aws ec2 describe-route-tables --filters Name=vpc-id,Values=<vpc-id>

# Check subnet associations
aws ec2 describe-subnets --subnet-ids <subnet-id>

# Verify security groups
aws ec2 describe-security-groups --group-ids <sg-id>

# Check instance public IP
aws ec2 describe-instances --instance-ids <instance-id>
