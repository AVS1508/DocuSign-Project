"""Form class declaration."""
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SelectField, BooleanField, SubmitField, IntegerField, DecimalField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length, URL)
from wtforms.fields.html5 import DateField
import pycountry

class VolunteerForm(FlaskForm):
    """Sign up for volunteering"""
    prefixName = SelectField('Prefix',[DataRequired()],choices=[('Mr.','Mr.'),('Mrs.','Mrs.'),('Miss','Miss'),('Ms.','Ms.'),('NIL','NIL')])
    firstName = StringField('First Name',[DataRequired()])
    lastName = StringField('Last Name',[DataRequired()])
    emailID = StringField('Email', [Email(message='Not a valid email address.'), DataRequired()])
    DOB = DateField('Date of Birth', format='%Y-%m-%d')
    phoneNumber = IntegerField()
    countryName = SelectField('Country of Residence', [DataRequired()], choices=[i.name for i in list(pycountry.countries)])
    volunteerHospitals = BooleanField()
    volunteerOrphanages = BooleanField()
    volunteerSchools = BooleanField()
    volunteerComputers = BooleanField()
    volunteerCommunity = BooleanField()
    volunteerArts = BooleanField()
    volunteerRemoteLocal = BooleanField()
    volunteerInPerson = BooleanField()
    volunteerRemoteInternational = BooleanField()
    submit = SubmitField('Submit')
    
class DonateForm(FlaskForm):
    """Make a donation"""
    prefixName = SelectField('Prefix',[DataRequired()],choices=[('Mr.','Mr.'),('Mrs.','Mrs.'),('Miss','Miss'),('Ms.','Ms.'),('NIL','NIL')])
    firstName = StringField('First Name',[DataRequired()])
    lastName = StringField('Last Name',[DataRequired()])
    emailID = StringField('Email', [Email(message='Not a valid email address.'), DataRequired()])
    DOB = DateField('Date of Birth', format='%Y-%m-%d')
    phoneNumber = IntegerField('Phone Number',[Length(max=16)])
    countryName = SelectField('Country of Residence', [DataRequired()], choices=[i.name for i in list(pycountry.countries)])
    donationCurrency = SelectField('Donation Currency',[DataRequired()],choices=[('$','$'),('£','£'),('€','€'),('¥','¥'),('₹','₹')])
    donationAmount = DecimalField('Donation Amount',[DataRequired()])
    donationCause = SelectField('Prefix',[DataRequired()],choices=[('Hospitals','Hospitals'),('Orphanages','Orphanages'),('Schools','Schools'),('Community Services','Community Services'),('Computer Classes','Computer Classes'),('Arts & Entertainment','Arts & Entertainment')])
    donationMessage = TextAreaField('Leave a message for our benefactors.',[Length(max=200)])
    submit = SubmitField('Submit')