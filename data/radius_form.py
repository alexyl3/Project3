from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, BooleanField


class RadiusForm(FlaskForm):
    words = StringField('Ключевые слова', validators=[])
    radius = IntegerField('Искать книги от продавцов в радиусе до:', validators=[])
    not_show = BooleanField('Не показывать мои объявления')
    submit = SubmitField('Искать')