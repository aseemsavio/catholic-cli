from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="catholic-cli",
    version="0.0.6",
    description="A Command Line Utility for Accessing Information Related to The Catholic Church",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Aseem Savio",
    author_email="aseemsavio3@gmail.com",
    url="https://github.com/aseemsavio/catholic-cli/blob/master/README.md",
    license="MIT",
    keywords="christianity, catholicism, catholic, christian, religion, cli",
    packages=find_packages(),
    include_package_data=True,
    data_files=[("catholic/pickles", ["catholic/pickles/canon.pickle",
                                      "catholic/pickles/catechism.pickle",
                                      "catholic/pickles/girm.pickle"
                                      ])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
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
