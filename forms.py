from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField, EmailField, TextAreaField, TelField, \
    TimeField, SelectField, DateField, SelectMultipleField
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
    info = TextAreaField("Немного о заведении")
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
    start_work_time = TimeField('Время начала работы мастера (по пол часа)', validators=[DataRequired()])
    end_work_time = TimeField('Время конца работы мастера (по пол часа)', validators=[DataRequired()])
    work_days = SelectMultipleField("Рабочие дни (пока кастыль и выбор через запятую 1,2,3,4", choices=[
        ('1', 'Понедельник',),
        ('2', 'Вторник'),
        ('3', 'Среда'),
        ('4', 'Четверг'),
        ('5', 'Пятница'),
        ('6', 'Суббота'),
        ('7', 'Воскресенье')])
    submit = SubmitField('Добавить')


class ChangeMasterForm(FlaskForm):
    name = StringField('Имя мастера', validators=[DataRequired()])
    start_work_time = TimeField('Время начала работы мастера (по пол часа)', validators=[DataRequired()])
    end_work_time = TimeField('Время конца работы мастера (по пол часа)', validators=[DataRequired()])
    work_days = SelectMultipleField("Рабочие дни (пока кастыль и выбор через запятую 1,2,3,4", choices=[
        ('1', 'Понедельник',),
        ('2', 'Вторник'),
        ('3', 'Среда'),
        ('4', 'Четверг'),
        ('5', 'Пятница'),
        ('6', 'Суббота'),
        ('7', 'Воскресенье')])
    submit = SubmitField('Изменить')


class AddProcessForm(FlaskForm):
    name = StringField('Название услуги', validators=[DataRequired()])
    duration = TimeField('Продолжительность услуги (по пол часа)', validators=[DataRequired()])
    info = TextAreaField("Информация об услуге")
    submit = SubmitField('Добавить')


class ChangeProcessForm(FlaskForm):
    name = StringField('Название услуги', validators=[DataRequired()])
    duration = TimeField('Продолжительность услуги (по пол часа)', validators=[DataRequired()])
    info = TextAreaField("Информация об услуге")
    submit = SubmitField('Изменить')


class RegisterCLientForm(FlaskForm):
    choices = [('1', '1'), ('2', '2'), ('3', '3')]
    name = StringField('Ваше имя', validators=[DataRequired()])
    phone_number = TelField('Номер телефона для связи', validators=[DataRequired()])
    process = SelectField('Выберете услугу', choices=[])
    date = DateField('Дата записи', validators=[DataRequired()])
    start_time = TimeField('Время записи', validators=[DataRequired()])
    submit = SubmitField('Записаться')
