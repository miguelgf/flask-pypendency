import glob
from typing import Optional

from flask import Flask
from pypendency.builder import ContainerBuilder
from pypendency.loaders.py_loader import PyLoader
from pypendency.loaders.yaml_loader import YamlLoader

__all__ = ["Pypendency"]


class Pypendency:
    def __init__(self, app: Optional[Flask] = None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        # Will search folders with this name under the files locations dir
        app.config.setdefault("PYPENDENCY_DI_FOLDER_NAME", "_dependency_injection")

        # List of absolute paths where to search for the folder name
        app.config.setdefault("PYPENDENCY_DISCOVER_PATHS", [app.root_path])

        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions["pypendency"] = None
        self._configure(app)

    def _configure(self, app: Flask) -> None:
        container = ContainerBuilder([])
        app.extensions["pypendency"] = container

        py_loader = PyLoader(app.extensions["pypendency"])
        yaml_loader = YamlLoader(app.extensions["pypendency"])

        di_folder_name = app.config.get("PYPENDENCY_DI_FOLDER_NAME")
        for registered_place in app.config.get("PYPENDENCY_DISCOVER_PATHS"):
            for di_folder in glob.glob(f"{registered_place}/**/{di_folder_name}", recursive=True):
                py_loader.load_dir(di_folder)
                yaml_loader.load_dir(di_folder)
