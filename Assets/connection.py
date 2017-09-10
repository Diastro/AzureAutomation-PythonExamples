"""
Python support for Azure automation is now public preview!
 
Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""

from automationassets import *

# get a connection (type azure service principal)
connection = get_automation_connection("connection-test-sp")
print connection["ApplicationId"]
print connection["CertificateThumbprint"]
print connection["TenantId"]
print connection["SubscriptionId"]

# handling non-existant connection
try:
    value = get_automation_certificate("non-existant-connection")
except AutomationAssetNotFound:
    print "connection not found."
