import sys

from geo2sql import converter

if __name__ == '__main__':
    paths = sys.argv[1:]

    if len(paths) < 1:
        raise Exception("No path(s) specified")

    for path in paths:
        converter.convert(path)

    sys.stdout.close()
