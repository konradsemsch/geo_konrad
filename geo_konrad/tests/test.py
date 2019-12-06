# Here we can include your basic package testing

from unittest import TestCase

import geo_konrad

class TestLocate(TestCase):
    def output_is_string(self):
        out = geo_konrad.locate_coordinates(52.375, 13.667)
        self.assertTrue(isinstance(out, basestring))