from __future__ import print_function
import sys
import json


def convert(path):
    try:
        with open(path, 'r') as f:
            geojson = json.loads(f.read())
            # Warning - Only looking at the exterior, hence skipping holes.
            coordinates = geojson['features'][0]['geometry']['coordinates'][0]

            coord_string = ", ".join(["{} {}".format(x, y) for x, y in coordinates])
            sql_polygon = u"POLYGON(({}))".format(coord_string)

            sys.stdout.write(sql_polygon)

    except IOError:
        print("No such file")
    except KeyError:
        print("File is not properly formatted")
