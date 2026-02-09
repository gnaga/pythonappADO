"""Setup configuration for myflaskapp."""

from setuptools import setup, find_packages

setup(
    name="myflaskapp",
    version="1.0.0",
    description="A sample Flask web application",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "flask>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "myflaskapp=myflaskapp.app:main",
        ],
    },
)
