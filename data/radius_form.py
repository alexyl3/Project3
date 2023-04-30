from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class RadiusForm(FlaskForm):
    radius = IntegerField('Искать книги от продавцов в радиусе до:', validators=[DataRequired()])
    submit = SubmitField('Искать')