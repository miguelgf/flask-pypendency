from setuptools import setup

with open("README.md", "r") as readme:
    README = readme.read()

version = "0.1.0"

setup(
    name="Flask-Pypendency",
    version=version,
    url="https://github.com/miguelgf/pypendency-flask",
    license="MIT License",
    author="Miguel González Flores",
    author_email="miguelgzflores@gmail.com",
    description="Flask extension for Pypendency, a dependency injection tool",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["flask_pypendency"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "Flask",
        "Pypendency"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
        "Framework :: Flask",
    ],
    python_requires=">=3.6",
)
