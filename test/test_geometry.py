import unittest
from naivert import *
from Geometry3D import *
class GeometryTest(unittest.TestCase):
    def test_get_tangential_vector(self):
        n = -y_unit_vector()
        in_vec = Vector(22,-1,0)
        self.assertEqual(get_tangential_vector(in_vec,n),22 * x_unit_vector())
        n = -y_unit_vector()
        in_vec = Vector(0,-1,0)
        self.assertEqual(get_tangential_vector(in_vec,n),Vector(0,0,0))