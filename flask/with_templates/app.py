# -*- coding: utf-8 -*-
import datetime

from flask import Flask, request, render_template

import config
from forms import ContactForm

__author__ = 'milex'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

class BlogPostModel(object):
    def __init__(self, form_data):
        self.title = form_data['title']
        self.text = form_data['text']

class Storage(object):
    obj = None
    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj

app.route('/', methods=['GET', 'POST'])
def home():
    validation_result = None
    current_date = datetime.datetime.now()
    storage = Storage()
    all_items = storage.items

    if request.method == 'POST':
        form = ContactForm(request.form)
        if form.validate():
            model = BlogPostModel(form.data)
            all_items.append(model)
    else:
        form = ContactForm()
    return render_template('home.html', form=form, items=all_items)

if __name__ == '__main__':
    app.run(debug=True)
