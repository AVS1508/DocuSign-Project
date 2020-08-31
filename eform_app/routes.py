import platform, subprocess, os, base64, ssl
from flask import render_template, request, make_response, redirect
from flask import current_app as app
from .forms import DonateForm, VolunteerForm
from .consts import access_token, account_id, base_url, client_user_id, authentication_method, base_path
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Tabs, Recipients, Document, RecipientViewRequest
import pdfkit


formData = None

# Constants
APP_PATH = os.path.dirname(os.path.abspath(__file__))

# Set FLASK_ENV to development if it is not already set
if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'development'

def _get_pdfkit_config():
    if platform.system() == 'Windows':
         return pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
    else:
         WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], stdout=subprocess.PIPE).communicate()[0].strip()
         return pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD) 

@app.route('/')
def home():
    return render_template('index.jinja2', template='home-template')

@app.route('/volunteer/', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        formData = request.form
        signer_name = request.form['prefixName']+" "+request.form['firstName']+" "+request.form['lastName']
        signer_email = request.form['emailID']
        signer_id = request.form['phoneNumber']
        signer_file_path = "static/pdfs/Volunteer-Form.pdf"
        signer_file_name = "Volunteer-Form"
        form_filled_type = "/signed/"
        return redirect(embedded_signing_ceremony(signer_email, signer_name, signer_id, signer_file_path, signer_file_name, form_filled_type), code=302)
    else:
        return render_template('volunteer.jinja2', form=VolunteerForm(), url=request.url)

@app.route('/donate/', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        formData = request.form
        signer_name = request.form['prefixName']+" "+request.form['firstName']+" "+request.form['lastName']
        signer_email = request.form['emailID']
        signer_id = request.form['phoneNumber']
        signer_file_path = "static/pdfs/Donation-Form.pdf"
        signer_file_name = "Donation-Form"
        form_filled_type = "/signed/"
        return redirect(embedded_signing_ceremony(signer_email, signer_name, signer_id, signer_file_path, signer_file_name, form_filled_type), code=302)
    else:
        return render_template('donate.jinja2', form=DonateForm(), url=request.url)

@app.route('/pdf_volunteer/', methods=['GET','POST'])
def pdf_volunteer():
    rendered = render_template('pdf_volunteer.jinja2', data=formData)
    pdf = pdfkit.from_string(rendered, False, configuration=_get_pdfkit_config(), options={'enable-local-file-access': None})
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Volunteer-Form.pdf'
    return response

@app.route('/pdf_donate/', methods=['GET','POST'])
def pdf_donate():
    rendered = render_template('pdf_donate.jinja2', data=formData)
    pdf = pdfkit.from_string(rendered, False, configuration=_get_pdfkit_config(), options={'enable-local-file-access': None})
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Donation-Form.pdf'
    return response

@app.route('/signed/', methods=['GET'])
def signed():
    return render_template('index-signed.jinja2', template='home-template')

def embedded_signing_ceremony(signer_email, signer_name, signer_id, signer_file_path, signer_file_name, form_filled_type):

    with open(os.path.join(APP_PATH, signer_file_path), "rb") as file:
        content_bytes = file.read()
    base64_file_content = base64.b64encode(content_bytes).decode('ascii')

    document = Document(document_base64 = base64_file_content, name = signer_file_name, file_extension = 'pdf', document_id = 1)

    signer = Signer(email = signer_email, name = signer_name, recipient_id = "1", routing_order = "1", client_user_id = signer_id)

    sign_here = SignHere(document_id = '1', page_number = '1', recipient_id = '1', tab_label = 'SignHereTab', x_position = '300', y_position = '650')
    
    signer.tabs = Tabs(sign_here_tabs = [sign_here])

    envelope_definition = EnvelopeDefinition(
        email_subject = "Please sign this document sent from the Python SDK",
        documents = [document], 
        recipients = Recipients(signers = [signer]),
        status = "sent"
    )

    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    
    results = envelope_api.create_envelope(account_id, envelope_definition=envelope_definition)

    envelope_id = results.envelope_id
    
    recipient_view_request = RecipientViewRequest(authentication_method = "email", client_user_id = signer_id, recipient_id = '1', return_url = base_url + form_filled_type, user_name = signer_name, email = signer_email)

    results = envelope_api.create_recipient_view(account_id, envelope_id, recipient_view_request = recipient_view_request)
    return results.url