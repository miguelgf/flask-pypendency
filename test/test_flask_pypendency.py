import os
from unittest import TestCase

from flask import Flask

from flask_pypendency import Pypendency
from test.resources.test_full.autodiscover1.a import A
from test.resources.test_full.autodiscover2.b import B


class TestFlaskPypendency(TestCase):
    def test_flask_pypendency(self):
        app = Flask(__name__)
        test_folder = os.path.dirname(os.path.abspath(__file__))
        app.config.from_mapping(
            PYPENDENCY_DI_FOLDER_NAME="_di",
            PYPENDENCY_DISCOVER_PATHS=[
                os.path.join(test_folder, "resources/test_full")
            ]
        )

        pypendency = Pypendency(app)

        with app.app_context():
            self.assertIsInstance(pypendency.container.get("test.resources.test_full.autodiscover1.a.A"), A)
            self.assertIsInstance(pypendency.container.get("test.resources.test_full.autodiscover2.b.B"), B)


