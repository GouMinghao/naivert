import unittest
from naivert import get_reflection_halfline,get_refraction_halfline,get_tangential_vector,inter_halfline_cpgs
from Geometry3D import *

class GeometryTest(unittest.TestCase):
    def test_get_tangential_vector(self):
        n = -y_unit_vector()
        in_vec = Vector(22,-1,0)
        self.assertEqual(get_tangential_vector(in_vec,n),22 * x_unit_vector())
        n = -y_unit_vector()
        in_vec = Vector(0,-1,0)
        self.assertEqual(get_tangential_vector(in_vec,n),Vector(0,0,0))

    def test_get_reflection_halfline(self):
        cpg = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
        hl1 = HalfLine(Point(0,0.5,0.5),Point(0.5,0.5,0))
        hl2 = HalfLine(Point(0.5,0.5,1),Point(0.5,0.5,0.5))
        self.assertEqual(get_reflection_halfline(hl1,cpg),HalfLine(Point(0.5,0.5,0),Vector(1,0,1)))
        self.assertEqual(get_reflection_halfline(hl2,cpg),HalfLine(Point(0.5,0.5,0),Vector(0,0,1)))

    def test_get_refraction_halfline(self):
        import math
        cpg = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
        hl1 = HalfLine(Point(0,0.5,0.5),Point(0.5,0.5,0))
        hl2 = HalfLine(Point(0.5,0.5,1),Point(0.5,0.5,0.5))
        self.assertEqual(get_refraction_halfline(hl1,in_n = 1, out_n = math.sqrt(2),cpg = cpg),HalfLine(Point(0.5,0.5,0),Vector(1,0,-math.sqrt(3))))
        self.assertEqual(get_refraction_halfline(hl2,in_n = 1, out_n = math.sqrt(2),cpg = cpg),HalfLine(Point(0.5,0.5,0),Vector(0,0,-1)))

    def test_inter_halfline_cpgs(self):
        import copy,math
        cpg = Parallelogram(origin(),x_unit_vector(),y_unit_vector())
        cpg1 = copy.deepcopy(cpg).move(z_unit_vector()+0.001 * x_unit_vector())
        cpg2 = copy.deepcopy(cpg1).move(z_unit_vector()+0.001 * y_unit_vector())
        p1 = Point(10,10,5)
        p2 = Point(0.4,0.6,2)
        hl = HalfLine(Point(10,10,5),Point(0.4,0.6,2))
        p,d = inter_halfline_cpgs(hl,[cpg,cpg1,cpg2])
        self.assertAlmostEqual(d,distance(p1,p2))
        self.assertEqual(p,p2)
        cpg.move(10*x_unit_vector())
        cpg1.move(10*x_unit_vector())
        cpg2.move(10*x_unit_vector())
        p,d = inter_halfline_cpgs(hl,[cpg,cpg1,cpg2])
        self.assertTrue(p is None)
        self.assertEqual(d,math.inf)
