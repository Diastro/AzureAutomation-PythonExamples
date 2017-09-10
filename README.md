# AzureAutomation-PythonExamples
Python2 example runbooks for Azure Automation

To report an issue or request an example please open an [issue](https://github.com/Diastro/AzureAutomation-PythonExamples/issues)

### Python SDK
The Azure Python2 SDK is build into Azure Automation. To use **any** of the Azure module simply import them from your runbooks like so :

```
from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage import CloudStorageAccount
from azure.storage.blob.models import ContentSettings, PublicAccess
...
```
Reference : [Azure Python SDK Documentation](https://azure-sdk-for-python.readthedocs.io/en/latest/#)

## Runbook examples
#### Automation assets
* [Connections](https://github.com/Diastro/AzureAutomation-PythonExamples/blob/master/Assets/connection.py)
* [Certificates](https://github.com/Diastro/AzureAutomation-PythonExamples/blob/master/Assets/certificates.py)
* [Credentials](https://github.com/Diastro/AzureAutomation-PythonExamples/blob/master/Assets/credentials.py)
* [Variables](https://github.com/Diastro/AzureAutomation-PythonExamples/blob/master/Assets/variables.py)

#### Automation runbook parameter
* [Runbook parameters](https://github.com/Diastro/AzureAutomation-PythonExamples/blob/master/Parameters/parameters.py)

#### RunAs (Azure service principal)
 * [List azure resource groups](https://github.com/Diastro/AzureAutomation-PythonExamples/blob/master/RunAs/azure-list-resource-group.py)
 * [Parallel start/stop azure vms](https://github.com/Diastro/AzureAutomation-PythonExamples/blob/master/RunAs/azure-parallel-start-vm.py)

## Reference
* [Azure Automation documentation](https://docs.microsoft.com/en-us/azure/automation/automation-runbook-types)
* [Azure Python SDK Documentation](https://azure-sdk-for-python.readthedocs.io/en/latest/#)
