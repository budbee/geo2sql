from distutils.core import setup

setup(
    name="geo2sql",
    version="1.0.0a1",
    author="David Nilsson",
    author_email="david.nilsson@budbee.com",
    packages=["geo2sql"],
    install_requires=[
        "mock",
    ],
    description="Convert geoJSON Polygons to SQL insert statements",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7"
    ],
    keywords="geoJSON GIS Polygon SQL",
    python_requires="=2.7"
)
