from unittest import TestCase
from unittest.mock import patch, call

from flask import Flask

from flask_pypendency import Pypendency


class TestLoader(TestCase):
    @patch("flask_pypendency.YamlLoader")
    @patch("flask_pypendency.PyLoader")
    def test_loader_default_values(self, py_loader, yaml_loader):
        """
        Specify the folders loads different routes
        """
        app = Flask(__name__)
        app.config.from_mapping(
            PYPENDENCY_DISCOVER_PATHS=["./_resources/test_loader"],
        )

        Pypendency(app)

        py_loader.return_value.load_dir.assert_has_calls([
            call("./_resources/test_loader/autodiscover1/_dependency_injection"),
            call("./_resources/test_loader/autodiscover2/_dependency_injection"),
        ])
        yaml_loader.return_value.load_dir.assert_has_calls([
            call("./_resources/test_loader/autodiscover1/_dependency_injection"),
            call("./_resources/test_loader/autodiscover2/_dependency_injection"),
        ])

    @patch("flask_pypendency.YamlLoader")
    @patch("flask_pypendency.PyLoader")
    def test_loader_configured_di_folder(self, py_loader, yaml_loader):
        """
        Specify the folders loads different routes
        """
        app = Flask(__name__)
        app.config.from_mapping(
            PYPENDENCY_DI_FOLDER_NAME="_di_folder1",
            PYPENDENCY_DISCOVER_PATHS=["./_resources/test_loader"],
        )

        Pypendency(app)

        py_loader.return_value.load_dir.assert_has_calls([
            call("./_resources/test_loader/autodiscover1/_di_folder1"),
        ])
        yaml_loader.return_value.load_dir.assert_has_calls([
            call("./_resources/test_loader/autodiscover1/_di_folder1"),
        ])

