import os
from dotenv import load_dotenv

from flask_testing import TestCase

from api import app, db
from api.accounts.models import User

load_dotenv()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        testdb_path = os.path.join("instance", "testdb.sqlite")
        os.remove(testdb_path)