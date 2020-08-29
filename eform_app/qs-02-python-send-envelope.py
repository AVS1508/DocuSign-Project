# Python3 Quick start example: send an envelope to be signed. The signer is notified by email
# Copyright (c) 2018 by DocuSign, Inc.
# License: The MIT License -- https://opensource.org/licenses/MIT

import base64, os
import ssl
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Tabs, Recipients, Document

# Settings
# Fill in these constants
#
# Obtain an OAuth access token from https://developers.docusign.com/oauth-token-generator
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjY4MTg1ZmYxLTRlNTEtNGNlOS1hZjFjLTY4OTgxMjIwMzMxNyJ9.eyJUb2tlblR5cGUiOjUsIklzc3VlSW5zdGFudCI6MTU5ODUzNTE4MywiZXhwIjoxNTk4NTYzOTgzLCJVc2VySWQiOiI3NmExNDM0Yy03YjFjLTQzYTAtODljZi1iODE3MDczNTQwOTciLCJzaXRlaWQiOjEsInNjcCI6WyJzaWduYXR1cmUiLCJjbGljay5tYW5hZ2UiLCJvcmdhbml6YXRpb25fcmVhZCIsInJvb21fZm9ybXMiLCJncm91cF9yZWFkIiwicGVybWlzc2lvbl9yZWFkIiwidXNlcl9yZWFkIiwidXNlcl93cml0ZSIsImFjY291bnRfcmVhZCIsImRvbWFpbl9yZWFkIiwiaWRlbnRpdHlfcHJvdmlkZXJfcmVhZCIsImR0ci5yb29tcy5yZWFkIiwiZHRyLnJvb21zLndyaXRlIiwiZHRyLmRvY3VtZW50cy5yZWFkIiwiZHRyLmRvY3VtZW50cy53cml0ZSIsImR0ci5wcm9maWxlLnJlYWQiLCJkdHIucHJvZmlsZS53cml0ZSIsImR0ci5jb21wYW55LnJlYWQiLCJkdHIuY29tcGFueS53cml0ZSJdLCJhdWQiOiJmMGYyN2YwZS04NTdkLTRhNzEtYTRkYS0zMmNlY2FlM2E5NzgiLCJhenAiOiJmMGYyN2YwZS04NTdkLTRhNzEtYTRkYS0zMmNlY2FlM2E5NzgiLCJpc3MiOiJodHRwczovL2FjY291bnQtZC5kb2N1c2lnbi5jb20vIiwic3ViIjoiNzZhMTQzNGMtN2IxYy00M2EwLTg5Y2YtYjgxNzA3MzU0MDk3IiwiYW1yIjpbImludGVyYWN0aXZlIl0sImF1dGhfdGltZSI6MTU5ODUzNTE4MCwicHdpZCI6IjU0YTkwZWFiLWEzNTItNDZiYy1hMDRlLTM0Nzc2MjMzMTIzOSJ9.lP8TwdYi7iCaoKv3otg9XOXlnMefE6z7zqp8AwJ6A6olXjSQoWsO-7UGXiDWjIbiHB8is6zmm29oxYHd_xBwarfRDeNATryewVMOAvjPSIR4Kf2TLyty2JPIsEfYlPI8tW5R4qWu7D7wouOkpU4BunulKvLMIPrD-37Q1QYqudYW9uk2nj2SOBDnIilL4XNKXwQ07keHpyP56cZz1soScUwO7cRuwvOLHgxABw-C4WoXFyIBIjFWGzeowA7neuus4QkRg3qn4kYL4ANx85Akf2faXCqopeIAPiW3Mw5K8jkqmgymnf21zyyOh5OfCgnZBu6oBDsWh-wI0wq3_w9Bhg'
# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture.
account_id = '11321217'
# Recipient Information:
signer_name = 'Loyal Customer'
signer_email = 'l.o.y.a.l.t.y.amaan@gmail.com'
# The document you wish to send. Path is relative to the root directory of this repo.
file_name_path = 'demo_documents/sample_assignment_5_answers.pdf'
base_path = 'https://demo.docusign.net/restapi'

# Constants
APP_PATH = os.path.dirname(os.path.abspath(__file__))

def send_document_for_signing():
    """
    Sends the document <file_name> to be signed by <signer_name> via <signer_email>
    """

    # Create the component objects for the envelope definition...
    with open(os.path.join(APP_PATH, file_name_path), "rb") as file:
        content_bytes = file.read()
    base64_file_content = base64.b64encode(content_bytes).decode('ascii')

    document = Document( # create the DocuSign document object 
        document_base64 = base64_file_content, 
        name = 'Example document', # can be different from actual file name
        file_extension = 'pdf', # many different document types are accepted
        document_id = 1 # a label used to reference the doc
    )

    # Create the signer recipient model 
    signer = Signer( # The signer
        email = signer_email, name = signer_name, recipient_id = "1", routing_order = "1")

    # Create a sign_here tab (field on the document)
    sign_here = SignHere( # DocuSign SignHere field/tab
        document_id = '1', page_number = '1', recipient_id = '1', tab_label = 'SignHereTab',
        x_position = '195', y_position = '147')

    # Add the tabs model (including the sign_here tab) to the signer
    signer.tabs = Tabs(sign_here_tabs = [sign_here]) # The Tabs object wants arrays of the different field/tab types

    # Next, create the top level envelope definition and populate it.
    envelope_definition = EnvelopeDefinition(
        email_subject = "Please sign this document sent from the Python SDK",
        documents = [document], # The order in the docs array determines the order in the envelope
        recipients = Recipients(signers = [signer]), # The Recipients object wants arrays for each recipient type
        status = "sent" # requests that the envelope be created and sent.
    )
    
    # Ready to go: send the envelope request
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.create_envelope(account_id, envelope_definition=envelope_definition)
    return results

# Mainline
results = send_document_for_signing()
print("\nEnvelope status: " + results.status + ". Envelope ID: " + results.envelope_id + "\n")
