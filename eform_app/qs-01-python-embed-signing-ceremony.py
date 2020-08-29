# Python3 Quick start example: embedded signing ceremony.
# Copyright (c) 2018 by DocuSign, Inc.
# License: The MIT License -- https://opensource.org/licenses/MIT
import base64, os
import ssl
from flask import Flask, request, redirect
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Tabs, Recipients, Document, RecipientViewRequest

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
# The url of this web application
base_url = 'http://localhost:5000'
client_user_id = '123' # Used to indicate that the signer will use an embedded
                       # Signing Ceremony. Represents the signer's userId within
                       # your application.
authentication_method = 'None' # How is this application authenticating
                               # the signer? See the `authenticationMethod' definition
                               # https://developers.docusign.com/esign-rest-api/reference/Envelopes/EnvelopeViews/createRecipient

# The API base_path
base_path = 'https://demo.docusign.net/restapi'

# Set FLASK_ENV to development if it is not already set
if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'development'

# Constants
APP_PATH = os.path.dirname(os.path.abspath(__file__))

def embedded_signing_ceremony():
    """
    The document <file_name> will be signed by <signer_name> via an
    embedded signing ceremony.
    """

    #
    # Step 1. The envelope definition is created.
    #         One signHere tab is added.
    #         The document path supplied is relative to the working directory
    #
    with open(os.path.join(APP_PATH, file_name_path), "rb") as file:
        content_bytes = file.read()
    base64_file_content = base64.b64encode(content_bytes).decode('ascii')

    # Create the document model
    document = Document( # create the DocuSign document object
        document_base64 = base64_file_content,
        name = 'Example document', # can be different from actual file name
        file_extension = 'pdf', # many different document types are accepted
        document_id = 1 # a label used to reference the doc
    )

    # Create the signer recipient model
    signer = Signer( # The signer
        email = 'l.o.y.a.l.t.y.amaan@gmail.com', name = 'Loyal Customer', recipient_id = "1", routing_order = "1",
        client_user_id = '123', # Setting the client_user_id marks the signer as embedded
    )

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

    #
    #  Step 2. Create/send the envelope.
    #
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.create_envelope(account_id, envelope_definition=envelope_definition)

    #
    # Step 3. The envelope has been created.
    #         Request a Recipient View URL (the Signing Ceremony URL)
    #
    envelope_id = results.envelope_id
    recipient_view_request = RecipientViewRequest(
        authentication_method = None, client_user_id = '123',
        recipient_id = '1', return_url = base_url + '/dsreturn',
        user_name = 'Loyal Customer', email = 'l.o.y.a.l.t.y.amaan@gmail.com'
    )

    results = envelope_api.create_recipient_view(account_id, envelope_id,
        recipient_view_request = 'true')

    #
    # Step 4. The Recipient View URL (the Signing Ceremony URL) has been received.
    #         Redirect the user's browser to it.
    #
    return results.url


# Mainline
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        return redirect(embedded_signing_ceremony(), code=302)
    else:
        return '''
            <html lang="en"><body><form action="{url}" method="post">
            <input type="submit" value="Sign the document!"
                style="width:13em;height:2em;background:#1f32bb;color:white;font:bold 1.5em arial;margin: 3em;"/>
            </form></body>
        '''.format(url=request.url)
@app.route('/dsreturn', methods=['GET'])
def dsreturn():
    return '''
        <html lang="en"><body><p>The signing ceremony was completed with
          status {event}</p>
          <p>This page can also implement post-signing processing.</p></body>
    '''.format(event=request.args.get('event'))

app.run()
