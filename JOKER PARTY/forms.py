from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, BooleanField ,DateField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    Name = StringField('NAME',
                           validators=[DataRequired(), Length(min=2, max=20)])
    Email = StringField('Email',
                        validators=[DataRequired(), Email()])
    Phone = StringField('Phone', validators=[DataRequired()])
    City = StringField('City',
                                     validators=[DataRequired()])
    Address = StringField('Address',
                                     validators=[DataRequired()])
    Date = StringField('Date',
                                     validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    def validate_Name(self, Name):
        user = User.query.filter_by(Name=Name.data).first()
        if user:
            raise ValidationError('That Name is taken. Please choose a different one.')

    def validate_email(self, Email):
        user = User.query.filter_by(Email=Email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')