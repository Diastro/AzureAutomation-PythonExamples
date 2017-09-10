"""
Python support for Azure automation is now public preview!
 
Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""

from automationassets import *

# get a credential
cred = get_automation_credential("credential-test")
print cred['username']
print cred['password']

# handling non-existant credential
try:
    value = get_automation_credential("non-existant-cred")
except AutomationAssetNotFound:
    print "Credential not found."
