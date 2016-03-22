# -*- coding: utf-8 -*-

from wtforms import Form
from wtforms import StringField, validators, ValidationError

__author__ = 'milex'


def full_name_validator(form, field):
    name_parts = field.data.split(' ')
    if len(name_parts) < 2:
        raise ValidationError('Name is not full!')


class ContactForm(Form):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=100), full_name_validator,
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35), validators.Email(),
    ])
