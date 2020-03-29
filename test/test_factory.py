from unittest import TestCase

from flask import Flask

from flask_pypendency import Pypendency


class TestFlaskFactory(TestCase):
    def test_factory(self):
        """
        Multiple applications have different container instances
        """
        app1 = self.__create_test_app()
        app2 = self.__create_test_app()

        self.assertNotEqual(app1.extensions["pypendency"], app2.extensions["pypendency"])

    def __create_test_app(self) -> Flask:
        app = Flask(__name__)
        Pypendency(app)

        return app
