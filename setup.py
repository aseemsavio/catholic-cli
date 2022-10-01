from setuptools import setup

setup(
    name="catholic-cli",
    version="0.0.1",
    description="A Command Line Utility for Accessing static Information Related to The Catholic Church",
    author="Aseem Savio",
    author_email="aseemsavio3@gmail.com",
    url="",
    license="",
    keywords="",
    install_requires=[
        "Click>=7",
        "rich>=12"
    ],
    entry_points={
        'console_scripts': [
            'catholic=catholic.catholic:cli',
        ],
    },
)
