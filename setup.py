import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="rlzero",
    version="0.1.0",
    description="Pygame Zero like API to teach 3d games programming based on Raylib",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/electronstudio/rlzero",
    author="Electron Studio",
    author_email="github@electronstudio.co.uk",
    license="LGPLv3+",
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["rlzero"],
    include_package_data=True,
    # entry_points={
    #     'console_scripts': [
    #         'rlzrun = rlzero.runner:main'
    #     ]
    # },
    scripts=['bin/rlzrun'],
    install_requires=["raylib==3.7.0post5"]
)
