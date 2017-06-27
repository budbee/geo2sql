import os
import unittest
from io import StringIO
from mock import patch

from geo2sql import converter

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'testdata.json')


class TestConvert(unittest.TestCase):
    def test_output(self):
        with patch('sys.stdout', new=StringIO()) as testOutput:
            converter.convert(TESTDATA_FILENAME)
            self.assertEqual(testOutput.getvalue(),
                             'POLYGON((18.0533817107 59.3378235714, 18.051915337 59.3374447557, 18.0502222539 59.3370103737, 18.0533817107 59.3378235714))\n')
