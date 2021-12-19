from setuptools import setup, find_packages

setup(
    name="prockset",
    version="1.0.0",
    author="rockset and Aarav Borthakur",
    author_email="api@rockset.io, gadhaguy13@gmail.com",
    description="Fork of Rockset python client source code with some changes",
    long_description="Fork of Rockset python client source code with some changes. Credit to the original [rockset library](https://pypi.org/project/rockset/).",
    long_description_content_type="text/markdown",
    url="https://github.com/gadhagod/pyrule-compendium",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["geojson", "requests", "requests-toolbelt", "protobuf", "docopt", "sqlalchemy", "texttable", "pyyaml"]
)