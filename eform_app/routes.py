import platform, subprocess, os
from flask import render_template, request, make_response
from flask import current_app as app
from .forms import DonateForm, VolunteerForm
import pdfkit

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
    return render_template('volunteer.jinja2', form=VolunteerForm())

@app.route('/donate/', methods=['GET', 'POST'])
def donate():
    return render_template('donate.jinja2', form=DonateForm())

@app.route('/pdf_volunteer/', methods=['POST'])
def pdf_volunteer():
    rendered = render_template('pdf_volunteer.jinja2', data=request.form)
    pdf = pdfkit.from_string(rendered, False, configuration=_get_pdfkit_config(), options={'enable-local-file-access': None})
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Volunteering-Form.pdf'
    return response

@app.route('/pdf_donate/', methods=['POST'])
def pdf_donate():
    rendered = render_template('pdf_donate.jinja2', data=request.form)
    pdf = pdfkit.from_string(rendered, False, configuration=_get_pdfkit_config(), options={'enable-local-file-access': None})
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Donation-Form.pdf'
    return response
