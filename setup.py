from distutils.core import setup
from setuptools import find_packages

setup(
    name="geo2sql",
    version="1.0.0a2",
    author="David Nilsson",
    author_email="david.nilsson@budbee.com",
    url="https://github.com/budbee/geo2sql",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=["mock"],
    test_suite="tests",
    description="Convert geoJSON MySQL Polygons",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7"
    ],
    keywords="geoJSON GIS Polygon SQL"
)
