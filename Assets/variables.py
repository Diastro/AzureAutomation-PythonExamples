"""
Python support for Azure automation is now public preview!
 
Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""

from automationassets import *

# get a variable
value = get_automation_variable("variable-test")
print value

# set a variable (value can be int/bool/string)
set_automation_variable("variable-test", "test-string")
set_automation_variable("variable-test", True)
set_automation_variable("variable-test", 4)

# handling non-existant variable
try:
    value = get_automation_variable("non-existant-variable")
except AutomationAssetNotFound:
    print "Variable not found."
