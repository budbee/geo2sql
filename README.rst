=======
Geo2Sql
=======

A small python package that parses GeoJSON files, extracts the containing polygons and writes the parsed data to stdout
on a MySQL friendly format, i.e. POLYGON((x y, x y, ..., x y)).

Setup and usage
---------------

Install by downloading the latest source file from https://github.com/budbee/geo2sql/releases or by using pip::

    pip install -e git://github.com/budbee/geo2sql.git@{ tag name }#egg={ desired egg name }

Run the module ``run.py`` located in the ``bin`` folder and specify one or more geoJSON files as arguments like so::

    python bin/run.py some/path/file1.json some/path/file2.json

