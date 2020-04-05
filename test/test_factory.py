from typing import Tuple
from unittest import TestCase

from flask import Flask

from flask_pypendency import Pypendency


class TestFlaskFactory(TestCase):
    def test_factory(self):
        """
        Multiple applications have different container instances
        """
        app1, _ = self.__create_test_app()
        app2, _ = self.__create_test_app()

        self.assertNotEqual(
            app1.extensions["pypendency"]["container"], app2.extensions["pypendency"]["container"]
        )

    def __create_test_app(self) -> Tuple[Flask, Pypendency]:
        app = Flask(__name__)
        pypendency = Pypendency(app)

        return app, pypendency

    def test_factory_different_contexts(self):
        """
        The container got depends on the flask app used in context
        """
        app1, pypendency1 = self.__create_test_app()
        app2, pypendency2 = self.__create_test_app()

        with app1.app_context():
            container_app1 = pypendency1.container

        with app2.app_context():
            container_app2 = pypendency2.container

        self.assertNotEqual(container_app1, container_app2)

    def test_factory_with_init_app(self):
        """
        The container got depends on the flask app used in context with the same instance of pypendency
        """
        app1 = Flask(__name__)
        app2 = Flask(__name__)

        pypendency = Pypendency()
        pypendency.init_app(app1)
        pypendency.init_app(app2)

        with app1.app_context():
            container_app1 = pypendency.container

        with app2.app_context():
            container_app2 = pypendency.container

        self.assertNotEqual(container_app1, container_app2)
