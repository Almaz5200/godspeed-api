from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.2.2"
DESCRIPTION = "A Godspeed task manager API wrapper"

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="godspeed_api",
    version=VERSION,
    author="Artem Trubacheev",
    author_email="almaz5200@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests",
        "dacite",
    ],
    keywords=["python", "godspeed"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
