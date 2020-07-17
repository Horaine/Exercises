from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Please enter your username"), Length(min=5, max=20)]),
    email = StringField('Email', 
                        validators=[DataRequired("Please enter your email"), Email()])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired("Please confirm your password"), EqualTo('password')])
    submit = SubmitField('Sign Up')




class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired("Please enter your email"), Email()])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')