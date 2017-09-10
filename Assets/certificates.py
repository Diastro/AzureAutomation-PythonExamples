"""
Python support for Azure automation is now public preview!
 
Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""

import binascii
from OpenSSL import crypto

from automationassets import *

# get a certificate
cert_binary = get_automation_certificate("AzureRunAsCertificate")

# convert to b64
cert_b64 = binascii.b2a_base64(cert_binary)
print cert_b64

# load certificate and dump the private key
pks12_cert = crypto.load_pkcs12(cert_binary)
pem_pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM, pks12_cert.get_privatekey())

# handling non-existant certificate
try:
    value = get_automation_certificate("non-existant-cert")
except AutomationAssetNotFound:
    print "Certificate not found."
