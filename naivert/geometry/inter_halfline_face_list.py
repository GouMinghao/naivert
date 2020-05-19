import math
from Geometry3D import Point, intersection, distance

def inter_halfline_face_list(hl,face_list):
    """
    **Input:**
    
    - hl: Geomrtry3D.HalfLine

    - faces: list of Faces

    **Output:**
    
    - (point,distance)

    - point: Geometry3D.Point of the first intersection point
    
    - distance: float of the distance between the intersection point and the start point of half line.
    
    - inter_face: the intersection Face
    """
    first_point = None
    least_distance = math.inf
    inter_face = None
    for face in face_list:
        inter_pt = intersection(hl,face.cpg)
        if inter_pt is not None:
            if isinstance(inter_pt,Point):
                dist = distance(inter_pt,hl.point)
                if  dist < least_distance:
                    least_distance = dist
                    first_point = inter_pt
                    inter_face = face
    return first_point,least_distance,inter_face

__all__ = ('inter_halfline_face_list',)