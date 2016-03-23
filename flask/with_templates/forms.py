# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, validators, ValidationError

__author__ = 'milex'


def full_name_validator(form, field):
    name_parts = field.data.split(' ')
    if len(name_parts) < 2:
        raise ValidationError('Name is not full!')


class ContactForm(Form):
    title = StringField(label='Title', validators=[
        validators.Length(min=4, max=100),
    ])
    text = StringField(label="Text", validators=[
        validators.Length(min=1, max=170),
    ])