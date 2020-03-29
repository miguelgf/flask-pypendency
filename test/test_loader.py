import os
from unittest import TestCase
from unittest.mock import patch, call

from flask import Flask

from flask_pypendency import Pypendency


class TestLoader(TestCase):
    def setUp(self) -> None:
        self.test_folder = os.path.dirname(os.path.abspath(__file__))

    @patch("flask_pypendency.YamlLoader")
    @patch("flask_pypendency.PyLoader")
    def test_loader_default_values(self, py_loader, yaml_loader):
        app = Flask(__name__)

        Pypendency(app)

        py_loader.return_value.load_dir.assert_has_calls([
            call(f"{self.test_folder}/resources/test_loader/autodiscover1/_dependency_injection"),
            call(f"{self.test_folder}/resources/test_loader/autodiscover2/_dependency_injection"),
        ])
        yaml_loader.return_value.load_dir.assert_has_calls([
            call(f"{self.test_folder}/resources/test_loader/autodiscover1/_dependency_injection"),
            call(f"{self.test_folder}/resources/test_loader/autodiscover2/_dependency_injection"),
        ])

    @patch("flask_pypendency.YamlLoader")
    @patch("flask_pypendency.PyLoader")
    def test_loader_configured_di_folder(self, py_loader, yaml_loader):
        """
        Specifying the folder's name loads different routes
        """
        app = Flask(__name__)
        app.config.from_mapping(
            PYPENDENCY_DI_FOLDER_NAME="_di_folder1",
        )

        Pypendency(app)

        py_loader.return_value.load_dir.assert_has_calls([
            call(f"{self.test_folder}/resources/test_loader/autodiscover1/_di_folder1"),
        ])
        yaml_loader.return_value.load_dir.assert_has_calls([
            call(f"{self.test_folder}/resources/test_loader/autodiscover1/_di_folder1"),
        ])

    @patch("flask_pypendency.YamlLoader")
    @patch("flask_pypendency.PyLoader")
    def test_loader_configured_di_discover_paths(self, py_loader, yaml_loader):
        """
        Specifying the folder's name loads different routes
        """
        app = Flask(__name__)
        app.config.from_mapping(
            PYPENDENCY_DISCOVER_PATHS=[f"{self.test_folder}/resources/test_loader/autodiscover2"]
        )

        Pypendency(app)

        py_loader.return_value.load_dir.assert_has_calls([
            call(f"{self.test_folder}/resources/test_loader/autodiscover2/_dependency_injection"),
        ])
        yaml_loader.return_value.load_dir.assert_has_calls([
            call(f"{self.test_folder}/resources/test_loader/autodiscover2/_dependency_injection"),
        ])

