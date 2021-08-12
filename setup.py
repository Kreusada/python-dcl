try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import setuptools

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name="dcl",
    version="0.0.1",
    author="Kreusada",
    author_email="kreusadaprojects@gmail.com",
    description="Python library used for diacritic manipulation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kreusada/python-dcl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"": ["*.json"]}
)