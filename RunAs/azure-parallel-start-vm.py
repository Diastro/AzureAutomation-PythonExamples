"""
Python support for Azure automation is now public preview!

Azure automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : http://azure-sdk-for-python.readthedocs.io/en/latest/index.html

"""
import sys
import threading

import automationassets
from azure.mgmt.compute import ComputeManagementClient


# replace with your own resource group
resource_group = ""
if resource_group == "":
    raise Exception("Please provide a resource group")

def get_automation_runas_credential(runas_connection):
    """ Returns credentials to authenticate against Azure resoruce manager """
    from OpenSSL import crypto
    from msrestazure import azure_active_directory
    import adal

    # Get the Azure Automation RunAs service principal certificate
    cert = automationassets.get_automation_certificate("AzureRunAsCertificate")
    pks12_cert = crypto.load_pkcs12(cert)
    pem_pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pks12_cert.get_privatekey())

    # Get run as connection information for the Azure Automation service principal
    application_id = runas_connection["ApplicationId"]
    thumbprint = runas_connection["CertificateThumbprint"]
    tenant_id = runas_connection["TenantId"]

    # Authenticate with service principal certificate
    resource = "https://management.core.windows.net/"
    authority_url = ("https://login.microsoftonline.com/" + tenant_id)
    context = adal.AuthenticationContext(authority_url)
    return azure_active_directory.AdalAuthentication(
        lambda: context.acquire_token_with_client_certificate(
            resource,
            application_id,
            pem_pkey,
            thumbprint)
    )


def start_vm(compute_client, rgn, vm_name):
    print vm_name + "Starting " + str(vm_name)
    async_vm_start = compute_client.virtual_machines.start(rgn, vm_name)
    async_vm_start.wait()
    print vm_name + "Started " + str(vm_name)
    sys.stdout.flush()


def stop_vm(compute_client, rgn, vm_name):
    print vm_name + "Stopping " + str(vm_name)
    async_vm_stop = compute_client.virtual_machines.power_off(rgn, vm_name)
    async_vm_stop.wait()
    print vm_name + "Stopped " + str(vm_name)
    sys.stdout.flush()


# Authenticate to Azure using the Azure Automation RunAs service principal
runas_connection = automationassets.get_automation_connection("AzureRunAsConnection")
azure_credential = get_automation_runas_credential(runas_connection)

compute_client = ComputeManagementClient(
    azure_credential,
    str(runas_connection["SubscriptionId"])
)

vm_list = compute_client.virtual_machines.list(resource_group_name=resource_group)

threads = []
for vm in vm_list:
    thread = threading.Thread(target=start_vm, args=[compute_client, resource_group, vm.name])
    thread.start()
    threads.append(thread)
    sys.stdout.flush()

print "Waiting on VMs operation to complete..."

for t in threads:
    t.join()

print "All thread joined."
