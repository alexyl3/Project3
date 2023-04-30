from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length
import re
from wtforms.validators import ValidationError
import requests


def is_correct_mobile_phone_number_ru(form, field):
    s = field.data
    if s.startswith('+7'):
        remainder = s[2:]
    elif s.startswith('8'):
        remainder = s[1:]
    else:
        raise ValidationError("Некорректный ввод номера телефона")

    remainder = re.sub(r'[ -]', '', remainder)
    if re.match(r'^\(\d{3}\)', remainder):
        remainder = re.sub(r'\(', '', remainder, 1)
        remainder = re.sub(r'\)', '', remainder, 1)
    if not bool(re.match(r'^\d{10}$', remainder)):
        raise ValidationError("Некорректный ввод номера телефона")
    return bool(re.match(r'^\d{10}$', remainder))


def is_correct_address(form, field):
    geocoder_request = \
        f"http://geocode-maps.yandex.ru/1.x/" \
        f"?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={field.data}&format=json"
    response1 = requests.get(geocoder_request)
    if not response1.json()["response"]["GeoObjectCollection"]["featureMember"]:
        raise ValidationError("Некорректный ввод адреса")


class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(message="Это поле обязательно для заполнения")])
    password = PasswordField('Пароль', validators=[DataRequired(message="Это поле обязательно для заполнения"),
                                                   Length(min=6, message="Минимальная длина пароля - 6")],
                             default='123456')
    password_again = PasswordField('Повторный пароль',
                                   validators=[DataRequired(message="Это поле обязательно для заполнения"),
                                               Length(min=6, message="Минимальная длина пароля - 6")])
    surname = StringField('Фамилия', validators=[DataRequired(message="Это поле обязательно для заполнения")])
    name = StringField('Имя', validators=[DataRequired(message="Это поле обязательно для заполнения")])
    address = StringField('Адрес', validators=[DataRequired(message="Это поле обязательно для заполнения"),
                                               is_correct_address])
    telephone = StringField('Номер телефона', validators=[DataRequired(message="Это поле обязательно для заполнения"),
                                                          is_correct_mobile_phone_number_ru])
    submit = SubmitField('Отправить')
