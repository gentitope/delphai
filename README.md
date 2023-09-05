# Task 1: Consistent backups script
Imagine we have a MongoDB cluster consisting of several data nodes running on managed
virtual machines in a cloud. We already have a script that creates snapshots of VM disks and
takes a hostname as the only parameter:
$ make-vm-snapshot vm-hostname
The task is to create a wrapper script around that script to make a consistent (see
https://www.mongodb.com/docs/manual/reference/method/db.fsyncLock/ method) snapshot of
one of the secondary nodes. The script will be called as follows:

$ yourscript

“mongodb://admin:password@vm-hostname1,vm-hostname2,vm-hostname3/admi
n?otherParams”

Expected deliverable: a script in python or similar (bash script would also be possible, however
it tends to be harder to achieve correct behavior there, especially in edge cases).
# Answer:
## Prerequisites
- python 
- Mongosh 

[Python Backup Wrapper Script](Task-1/backup.py)

# Task 2: Design database setup for microservices
We have two identical environments — test and production — with many services deployed
onto k8s clusters.
These services each need an isolated Postgres database. Developers should have read-write
access to all services in test environment and read-only in production.
The task is to outline a proposal (as a list of key action items and/or a dozen of sentences) on
how this database setup could be implemented inside the two environments. We might discuss
this setup and your proposal in more detail in the next interview round.
## Some points to consider:
● Managed or on-premise

● Single server or a cluster

● Single server/cluster, server/cluster per environment or server/cluster per application

● How to manage and provision accounts for applications and people

# Proposed Solution:
## Production Architecture
!["Microservice Architecture"](Task-2/image/delphai-prod.jpg?raw=true)

## Development Architecture
!["Microservice Architecture"](Task-2/image/delphai-dev.jpg?raw=true)


## Benefits
### This solution has a number of benefits:

- Simple services - each service consists of a small number of subdomains and is easier to understand and maintain
- Team autonomy - a team can develop, test and deploy their service independently of other teams
- Fast deployment pipeline - each service is fast to test since it’s relatively small, and can be deployed independently
- Support multiple technology stacks - different services can use different technology stacks/language and can be upgraded independently

## Drawbacks
### This solution has a number of (potential) drawbacks:

- Some distributed operations might be complex, and difficult to understand and troubleshoot
- High cost of management

### Considered points:
- AWS EKS 
- Microservice architecture with data in the database per service pattern for productionv - Data autonomy, minimize dependencies and best practices.
- Dev and Staging should use shared database pattern, as the name suggests, it allows multiple services to access and store data in the same database server but different schema - Cost Management.
- Seperate read and write operation from the application connection - Optimize Performance.
- Seperate production db server from dev and staging db server - Environment Isolation.
- AWS aurora with read replica and multi AZ enabled setup - High Availabilty.
- Granularly manage DB access using IAM Authentication - Better control over access management.
- DB Server is setup on private network - Security measures.