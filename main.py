from flask import Flask, render_template, make_response, request, session, redirect
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField, EmailField, TextAreaField, TelField
from wtforms.validators import DataRequired
from data import db_session
from data.admin import Admin
from data.master import Master
from data.process import Process
from data.record import Record
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import Flask, render_template
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


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
    phone_number = TelField('Номер телофона организации', validators=[DataRequired()])
    info = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query().get(user_id)


def set_password(self, password):
    self.hashed_password = generate_password_hash(password)


def check_password(self, password):
    return check_password_hash(self.hashed_password, password)


@app.route('/login', methods=['GET', 'POST'])
def login():  # Позже переделаю
    pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def reqister():  # Позже переделаю
    pass


@app.route("/")
def index():  # Позже переделаю
    return "Hello, World!"


def main():
    db_session.global_init("db/base.db")
    app.run()


if __name__ == '__main__':
    main()