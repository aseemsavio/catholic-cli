from setuptools import setup, find_packages

from catholic.version import version

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="catholic-cli",
    version=version,
    description="A Command Line Utility for Accessing Information Related to The Catholic Church",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Aseem Savio",
    author_email="aseemsavio3@gmail.com",
    url="https://github.com/aseemsavio/catholic-cli/blob/master/README.md",
    license="MIT",
    keywords="christianity, catholicism, catholic, christian, religion, cli",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    data_files=[("catholic/pickles", ["catholic/pickles/canon.pickle",
                                      "catholic/pickles/catechism.pickle",
                                      "catholic/pickles/girm.pickle"
                                      ]),
                ("catholic/index", ["catholic/index/canon_index/_MAIN_1.toc",
                                    "catholic/index/canon_index/MAIN_jcfftbwmodlertj6.seg",
                                    "catholic/index/canon_index/MAIN_WRITELOCK",
                                    "catholic/index/catechism_index/_MAIN_1.toc",
                                    "catholic/index/catechism_index/MAIN_WRITELOCK",
                                    "catholic/index/catechism_index/MAIN_x9ce2efhbz9dvnt0.seg",
                                    "catholic/index/missal_index/_MAIN_1.toc",
                                    "catholic/index/missal_index/MAIN_jg57nqsiitr2bdya.seg",
                                    "catholic/index/missal_index/MAIN_WRITELOCK"
                                    ])
                ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'typer[all]>=0.7.0',
        "Click>=7",
        "rich>=12",
        "questionary>=1.10.0",
        "Whoosh==2.7.4"
    ],
    entry_points={
        'console_scripts': [
            'catholic=catholic.catholic:cli',
        ],
    },
)
