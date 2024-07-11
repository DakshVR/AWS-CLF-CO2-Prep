
#! How to choose an AWS region?
#  As AWS has regions all around the world, it really depends on where you are launching your new application.
#* BUT, there are some fcators that needs to be considered.
#? Compliance with data governance and legal requirements.
#? Proximity to customers.
#? Latency.
#? Available services. with some regions having more services than others.
#? Cost. pricing may vary from region to region.

#! AWS Avilability Zones
# Each region has multiple availability zones.
# Each availability zone is a data center.
# Each availability zone is isolated from the other.
# Each availability zone is connected to the other with high-speed, low-latency network.
# Each availability zone is a separate failure zone.
# Each availability zone is a separate power source.

#! AWS Points of Presence
# AWS has points of presence all around the world.
# These are edge locations.
# These are used for caching content.

#! AWS Console
# AWS Global services.
#     Identity and Access Management (IAM)
#     Route 53 (DNS service)
#     CloudFront (CDN)
#     WAF (Web Application Firewall)
#       AWS Shield (DDoS protection)


#! ***************** Shared Responsibility Model ***************

#? Customer 
#? Responsibilty for security in the cloud
#    Customer Data
#    Platform, applications, identity and access management
#    Operating System, network, firewall configuration
#    Client-side data encryption and data integrity authentication
#    Network traffic protection(Encryption, VPN, Integrity, identity)
#    Server-side encryption(File system And/or Data)

#? AWS 
#? Responsibility for security of the cloud
#    *Software
#           Compute, storage, database, networking
#    *Hardware/AWS Global Infrastructure
#           Regions, Availability Zones, Edge Locations

# AWS Acceptable Use Policy

# No illegal, harmful, or offensive use of services.
# No security violations.
# No network abuse.
# No email spamming.
# No hacking.
# No distribution of malware.

#? Resources:
# https://aws.amazon.com/compliance/shared-responsibility-model/
