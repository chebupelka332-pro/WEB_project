from flask import Flask, render_template, make_response, request, session, redirect
from data.admin import Admin
from data.master import Master
from data.process import Process
from data.record import Record
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from forms import *
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(Admin, int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Admin).filter(Admin.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/profile")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(Admin).filter(Admin.login == form.login.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        
        user = Admin(
            name=form.name.data,
            login=form.login.data,
            info=form.info.data,
            number=form.phone_number.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, login=current_user.login,
                           number=current_user.number, info=current_user.info, id=current_user.id)


@app.route('/profile/change_profile', methods=['GET', 'POST'])
@login_required
def change_profile():
    form = ChangeProfileForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.old_password.data):
            return render_template('change_profile.html', title='Изменение профиля', form=form,
                                   message="Пароль не верный")
        if form.new_password.data != form.new_password_again.data:
            return render_template('change_profile.html', title='Изменение профиля', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if form.login.data in [elem.login for elem in db_sess.query(Admin).filter(Admin.id != current_user.id).all()]:
            return render_template('change_profile.html', title='Изменение профиля', form=form,
                                   message="Пользователь с таким логином уже есть")

        current_user.name = form.name.data
        current_user.login = form.login.data
        current_user.number = form.phone_number.data
        current_user.info = form.info.data
        current_user.set_password(form.new_password.data)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/profile')
    return render_template('change_profile.html', title='Изменение профиля', form=form)


@app.route("/profile/timeline")
@login_required
def timeline():  # Заготовка для таймлайна
    return 'Здесь должен быть таймлайн'


@app.route("/profile/masters")
@login_required
def masters():
    db_sess = db_session.create_session()
    data = db_sess.query(Master).filter(Master.admin_id == current_user.id)
    return render_template('masters.html', masters_data=data)


@app.route('/profile/add_masters', methods=['GET', 'POST'])
@login_required
def add_masters():
    form = AddMasterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        master = Master(
            name=form.name.data,
            admin_id=current_user.id,
            start_work_time=form.start_work_time.data.strftime('%H:%M'),
            end_work_time=form.end_work_time.data.strftime('%H:%M'),
            work_days=form.work_days.data
        )
        db_sess.add(master)
        db_sess.commit()
        return redirect('/profile/masters')
    return render_template('add_masters.html', title='Добавление мастера', form=form)


@app.route('/profile/change_masters/<id>', methods=['GET', 'POST'])
@login_required
def change_masters(id):
    form = ChangeMasterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        master = db_sess.query(Master).filter(Master.id == id).first()
        master.name = form.name.data
        master.start_work_time = form.start_work_time.data.strftime('%H:%M')
        master.end_work_time = form.end_work_time.data.strftime('%H:%M')
        master.work_days = form.work_days.data
        db_sess.merge(master)
        db_sess.commit()
        return redirect('/profile/masters')
    return render_template('change_masters.html', title='Изменение мастера', form=form)


@app.route('/profile/delete_masters/<id>', methods=['GET', 'POST'])
@login_required
def delete_masters(id):
    db_sess = db_session.create_session()
    db_sess.query(Master).filter(Master.id == id).delete()
    db_sess.commit()
    return redirect('/profile/masters')


@app.route("/profile/process")
def process():   # Заготовка для вкладки услуг
    return 'Здесь должна быть вкалдка с услугами'


@app.route('/record/<admin_id>')
def record(admin_id):  # Заготовка для записи
    return 'Здесь должна быть страницы для записи клиента на услугу'


def main():
    db_session.global_init("db/base.db")
    app.run()


if __name__ == '__main__':
    main()