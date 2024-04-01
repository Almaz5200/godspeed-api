from setuptools import setup, find_packages

VERSION = "0.1.1"
DESCRIPTION = "A Godspeed task manager API wrapper"

setup(
    name="godspeed_api",
    version=VERSION,
    author="Artem Trubacheev",
    author_email="almaz5200@gmail.com",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests",
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
