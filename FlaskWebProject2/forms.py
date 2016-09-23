from flask_wtf import Form, csrf
from wtforms import RadioField, StringField, TextField, TextAreaField, SubmitField, PasswordField, SelectField, Label
class Registering(Form):
    """description of class"""
name = TextField("name")
pwd = PasswordField("pwd")
email = TextField("email")
addr=TextAreaField("addr")
sex=RadioField('Gender', choices=[('M', 'Male'),('F','Female')])
submit = SubmitField('Submit')

