from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, RadioField, SubmitField
from wtforms.validators import InputRequired, Length


class CourseForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    enrolment_num = StringField('GIC Enrolment Number', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    course_rating = RadioField('Pick One',
                               choices=['Very Well', 'Well', 'Average', 'Poorly', 'Very Poorly'],
                               validators=[InputRequired()])
    submit = SubmitField('Submit')

