from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return "Hello, World!"


def main():
    db_session.global_init("db/base.db")
    app.run()


if __name__ == '__main__':
    main()