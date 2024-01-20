from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, DateField, TextAreaField, SelectField, SelectMultipleField, \
    widgets
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'patricks_most_secret_key'


class BasicForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    dob = DateField('Date of Birth')
    position = SelectField(u'Position Interest',
                           choices=[('Developer', 'Lightning Labs Developer'), ('Janitor', 'Janitor'),
                                    ('Astronaut', 'Astronaut')])
    employment_type = RadioField(u'Employment Type',
                                 choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'),
                                          ('Weekends', 'Weekends')])
    skills = SelectMultipleField('Skills',
                                 choices=[('Python', 'Python'), ('Javascript', 'Javascript'), ('Java', 'Java'),
                                          ('Cooking', 'Cooking'), ('Nun-Chucks', 'Nun-Chucks'),
                                          ('HTML/CSS', 'HTML/CSS')],
                                 option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False))
    submit = SubmitField('Submit', validators=[DataRequired()])


class GreenEggsAndHam(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])


@app.route('/')
def index():
    return render_template('index.html')


# Basic Survey
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = BasicForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        position = form.position.data
        employment_type = form.employment_type.data
        skills = form.skills.data
        string_output = (
            f"Hello, {first_name} {last_name}, Your birthday is {dob}, You're applying for our {position} position! You "
            f"would like to work {employment_type}. Your skills include {skills}.")
        return string_output
    return render_template('form.html', form=form)


# Green Eggs and Ham Survey
@app.route('/name_form_green_eggs', methods=['GET', 'POST'])
def name_form_green_eggs():
    form = GreenEggsAndHam()
    if form.validate_on_submit():
        name = form.name.data
        string_output = (
            f"Hello, {name}.")
        return string_output
    return render_template('name_form_green_eggs.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
