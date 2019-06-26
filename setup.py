import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="richlib",
    version="0.0.2",
    description="Pygame Zero like API to teach 3d games programming based on Raylib",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/electronstudio/richlib",
    author="Electron Studio",
    author_email="github@electronstudio.co.uk",
    license="LGPLv3+",
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["richlib"],
    include_package_data=True,
    install_requires=["raylib"]
)
