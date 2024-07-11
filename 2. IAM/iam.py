
#! IAM: Users & Groups

#* IAM is a global service.
# IAM = Identity and Access Management
# Root account is the account created when you create your AWS account.
# Root account has full admin access. Should not be used or shared.

#! It is not best practice to use the root account for daily tasks. So, we create users and groups.

# Users: People within your organization. can be grouped.
# USers don't have to belong to a group. and can belong to multiple groups.

# Groups: Collection of users. Each user in a group will inherit the permissions of the group.
# Groups can only contain users, not other groups.

#! IAM: Permissions

# Users or groups can be assigned JSON documents called policies.
# Policies: JSON documents that define permissions for users.
# In AWS you can apply least privilege principle: don't give more permissions than needed to a user.

#! IAM: Policies Inheritance

#! IAM Policies Structure


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}

#* Read only policy
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:GenerateCredentialReport",
                "iam:GenerateServiceLastAccessedDetails",
                "iam:Get*",
                "iam:List*",
                "iam:SimulateCustomPolicy",
                "iam:SimulatePrincipalPolicy"
            ],
            "Resource": "*"
        }
    ]
}

#  Consists of:
#       Version: the version of the policy language. always include "2012-10-17"
#       Id: an identifier for the policy. (optional)
#       Statement: the main section of the policy. Consists of an array of objects, may contain multiple objects.

# Each statement consists of:
#       Sid: an optional identifier for the statement.
#       Effect: whether the statement allows or denies access.
#       Principal: the account, user, role, or service to which the policy is applied.
#       Action: the list of actions this policy allows or denies.
#       Resource: the list of resources to which the actions apply.
#       Condition: the conditions under which the policy is in effect.