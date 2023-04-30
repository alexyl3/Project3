from flask_wtf import FlaskForm
from wtforms import SubmitField


class DeleteBookForm(FlaskForm):
    submit = SubmitField('Удалить', validators=[])
