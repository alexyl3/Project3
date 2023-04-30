from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField
from wtforms.validators import DataRequired


class AddBookForm(FlaskForm):
    title = StringField('Название книи', validators=[DataRequired()])
    author = StringField('Автор', validators=[DataRequired()])
    year = IntegerField('Год издания', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    condition = SelectField('Состояние', choices=['Новая', 'Хорошее', 'Удовлетворительное', 'Плохое'],
                            validators=[DataRequired()])
    submit = SubmitField('Выставить')
