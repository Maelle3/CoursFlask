
import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


ma = Marshmallow()

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/')
    def index():
        return '<h1>ECM Bonjour</h1>'

    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html', name=name)

    @app.route('/professor')
    def prof_api_route():
        return {
            "name": "Adrien",
            "birthday": "02 January",
            "age": 85,
            "sex": None,
            "friends": ["Amadou", "Mariam"]
        }

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    ma.init_app(app)

    db.init_app(app)
    from tasks.models import Task
    migrate = Migrate(app, db)

    from tasks.serializers import TaskSchema

    @app.route('/todoz')
    def my_api_route():
        tasks = Task.query.all()
        return {"results": TaskSchema(many=True).dump(tasks)}


    return app


