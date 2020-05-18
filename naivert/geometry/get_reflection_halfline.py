from Geometry3D import HalfLine, Point,intersection 
from .get_tangential_vector import get_tangential_vector

def get_reflection_halfline(in_hl,cpg):
    '''
    ** Input: **

    - in_hl: Geometry3D.HalfLine of input half line.

    - cpg: Geometry3D.ConvexPolygen of the intersection convex polygen

    ** Output: **

    - out_hl: Geometry3D.HalfLine of output half line.
    '''
    out_hl_point = intersection(in_hl,cpg)
    if out_hl_point is None:
        return None
    if not isinstance(out_hl_point,Point):
        return None
    normal = cpg.plane.n
    if normal * in_hl.vector < 0:
        normal = - normal
    in_vec = in_hl.vector
    tan_vec = get_tangential_vector(in_vec,normal)
    out_vec = 2 * tan_vec - in_vec
    return HalfLine(out_hl_point,out_vec)

__all__ = ('get_reflection_halfline',)