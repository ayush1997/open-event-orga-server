"""Copyright 2015 Rafal Kowalski"""
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from flask.ext.admin.form.fields import DateTimeField

from open_event.models.speaker import Speaker
from ...helpers.helpers import get_event_id


def get_speakers():
    return Speaker.query.filter_by(event_id=get_event_id())


class SessionForm(Form):
    title = StringField('Title')
    subtitle = StringField('Subtitle')
    abstract = TextAreaField('Abstract')
    description = TextAreaField('Description')
    start_time = DateTimeField('Start Time')
    end_time = DateTimeField('End Time')
    type = StringField('Type')
    level = StringField('Level')
    speakers = QuerySelectMultipleField(query_factory=get_speakers, allow_blank=True)