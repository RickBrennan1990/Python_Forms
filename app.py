from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, DateField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'patricks_most_secret_key'  # Replace with a real secret key

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])
    DOB = DateField('DOB')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        DOB = form.DOB.data
        return f"Hello, {name}, Your birthday is {DOB}!"
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
