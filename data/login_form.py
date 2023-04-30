from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(message="Это поле обязательно для заполнения")])
    password = PasswordField('Пароль', validators=[DataRequired(message="Это поле обязательно для заполнения"),
                                                   Length(min=6, message="Минимальная длина пароля - 6")])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
