## Mastering IAM: Using Boto3 to Manage AWS Resources with Python Scripts


If you’re getting started with AWS automation, **Boto3** is the go-to Python library. It’s the official AWS SDK for Python that makes it easy to interact with AWS resources directly from your scripts.  

This repository contains a collection of Python scripts I built while practicing AWS IAM (Identity and Access Management) automation. The scripts cover common IAM tasks such as creating users, groups, and roles, attaching policies, and listing or updating resources.

With IAM, you can:  
- Create and manage users  
- Set up groups and roles  
- Attach and manage permissions with policies  
- List and update IAM resources  

These scripts give you a quick starting point for learning IAM automation with Python.

---

## Repository Structure

| File | Description |
|------|-------------|
| `addusertogroup.py` | Adds an IAM user to a group. |
| `alliampolicies.py` | Lists all available IAM policies. |
| `attachiampolicytorole.py` | Attaches an IAM policy to a role. |
| `attachpolicytogroup.py` | Attaches an IAM policy to a group. |
| `attachuserpolicy.py` | Attaches a policy directly to a user. |
| `creategroup.py` | Creates a new IAM group. |
| `createuser.py` | Creates a new IAM user. |
| `iam.md` | Notes and usage instructions for managing IAM with Boto3. |
| `iampolicy.py` | Creates a custom IAM policy. |
| `iamrole.py` | Creates a new IAM role. |
| `iamuserslist.py` | Lists all IAM users in the account. |
| `userupd.py` | Updates user information. |

---

## Prerequisites

Before running the scripts, ensure you have:

- **Python 3.7+** installed  
- **Boto3** installed  
  ```bash
  pip install boto3
````

* **AWS credentials** configured (via `aws configure` or environment variables).
  You’ll need IAM permissions to run these operations.

---


## How to use the files

Run any script with:

```bash
python script_name.py
```

Example:

```bash
python createuser.py
```


---


## Notes

* IAM operations can affect account security. Test in **non-production environments** first.
* Customize the scripts as needed (e.g., user names, policy ARNs, or role definitions).
* Some scripts are basic examples — you may want to add error handling or logging for production use.

---
