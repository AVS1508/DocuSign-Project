from flask import url_for, render_template, redirect
from flask import current_app as app
from .forms import DonateForm, VolunteerForm


@app.route('/')
def home():
    return render_template('index.jinja2',
                           template='home-template')


@app.route('/volunteer/', methods=('GET', 'POST'))
def volunteer():
    form = VolunteerForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('volunteer.jinja2',
                           form=form,
                           template='form-template')


@app.route('/donate/', methods=('GET', 'POST'))
def donate():
    form = DonateForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('donate.jinja2',
                           form=form,
                           template='form-template')


@app.route('/success/', methods=('GET', 'POST'))
def success():
    return render_template('success.jinja2',
                           template='success-template')
