from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="catholic-cli",
    version="0.0.1",
    description="A Command Line Utility for Accessing Information Related to The Catholic Church",
    long_description=readme,
    author="Aseem Savio",
    author_email="aseemsavio3@gmail.com",
    url="",
    license="",
    keywords="christianity, catholicism, catholic, christian, religion, cli",
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
