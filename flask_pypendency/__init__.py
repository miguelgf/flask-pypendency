import glob
from typing import Optional

from flask import Flask, current_app
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
        app.config.setdefault("PYPENDENCY_DI_FOLDER_NAME", "_dependency_injection")
        app.config.setdefault("PYPENDENCY_DISCOVER_PATHS", [app.root_path])

        self._configure(app)

    def _configure(self, app: Flask) -> None:
        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions["pypendency"] = {"container": ContainerBuilder([])}

        py_loader = PyLoader(app.extensions["pypendency"]["container"])
        yaml_loader = YamlLoader(app.extensions["pypendency"]["container"])

        di_folder_name = app.config.get("PYPENDENCY_DI_FOLDER_NAME")
        for registered_place in app.config.get("PYPENDENCY_DISCOVER_PATHS"):
            for di_folder in glob.glob(f"{registered_place}/**/{di_folder_name}", recursive=True):
                py_loader.load_dir(di_folder)
                yaml_loader.load_dir(di_folder)

    @property
    def container(self) -> ContainerBuilder:
        return current_app.extensions["pypendency"]["container"]
