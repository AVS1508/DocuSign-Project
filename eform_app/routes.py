from flask import render_template, request, make_response
from flask import current_app as app
from .forms import DonateForm, VolunteerForm
import pdfkit

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
    pdf = pdfkit.from_string(rendered, False, {'enable-local-file-access': None})
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Volunteering-Form.pdf'
    return response

@app.route('/pdf_donate/', methods=['POST'])
def pdf_donate():
    rendered = render_template('pdf_donate.jinja2', data=request.form)
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=Donation-Form.pdf'
    return response

if __name__ == '__main__':
    app.run(threaded=False, port=5000)