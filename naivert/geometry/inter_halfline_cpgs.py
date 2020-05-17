import math
from Geometry3D import Point, intersection, distance

def inter_halfline_cpgs(hl,cpgs):
    '''
    ** Input: **
    
    - hl: Geomrtry3D.HalfLine

    - cpgs: list of Geometry3D.ConvexPolygen

    ** Output: **
    
    - (point,distance)

    - point: Geometry3D.Point of the first intersection point
    
    - distance: float of the distance between the intersection point and the start point of half line.
    '''
    first_point = None
    least_distance = math.inf
    for cpg in cpgs:
        inter_pt = intersection(hl,cpg)
        if inter_pt is not None:
            if isinstance(inter_pt,Point):
                dist = distance(inter_pt,hl.point)
                if  dist < lease_distance:
                    least_distance = dist
                    first_point = inter_pt
    return first,inter_pt
