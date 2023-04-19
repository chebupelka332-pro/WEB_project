from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField, EmailField, TextAreaField, TelField, \
    TimeField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    name = StringField('Название организации', validators=[DataRequired()])
    login = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    phone_number = TelField('Номер телефона организации', validators=[DataRequired()])
    info = TextAreaField("Немного о себе")
    submit = SubmitField('Зарегистрироваться')


class ChangeProfileForm(FlaskForm):  # Форма для изменения профиля по ссылке /change_profile
    name = StringField('Новое название организации', validators=[DataRequired()])
    login = EmailField('Новая почта', validators=[DataRequired()])
    old_password = PasswordField('Старый пароль', validators=[DataRequired()])
    new_password = PasswordField('Новый пароль', validators=[DataRequired()])
    new_password_again = PasswordField('Повторите новый пароль', validators=[DataRequired()])
    phone_number = TelField('Номер телефона организации', validators=[DataRequired()])
    info = TextAreaField("Информация о заведении")
    submit = SubmitField('Изменить')


class AddMasterForm(FlaskForm):
    name = StringField('Имя мастера', validators=[DataRequired()])
    start_work_time = TimeField('Время начала работы мастера', validators=[DataRequired()])
    end_work_time = TimeField('Время конца работы мастера', validators=[DataRequired()])
    work_days = TextAreaField("Рабочие дни (пока кастыль и выбор через запятую 1,2,3,4", validators=[DataRequired()])
    submit = SubmitField('Добавить')


class ChangeMasterForm(FlaskForm):
    name = StringField('Имя мастера', validators=[DataRequired()])
    start_work_time = TimeField('Время начала работы мастера', validators=[DataRequired()])
    end_work_time = TimeField('Время конца работы мастера', validators=[DataRequired()])
    work_days = TextAreaField("Рабочие дни (пока кастыль и выбор через запятую 1,2,3,4", validators=[DataRequired()])
    submit = SubmitField('Изменить')