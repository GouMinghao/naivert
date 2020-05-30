from Geometry3D import HalfLine, Point,angle, intersection, get_eps
from .get_tangential_vector import get_tangential_vector
import math
def get_refraction_halfline(in_hl,in_n,out_n,cpg):
    """
    **Input:**

    - in_hl: Geometry3D.HalfLine of input half line.

    - in_n: float of the inner material refraction rate

    - out_n: float of the outer material refraction rate

    - cpg: Geometry3D.ConvexPolygon of the intersection convex polygon

    **Output:**

    - out_hl: Geometry3D.HalfLine of output half line.
    """
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
    sin_theta_input = math.sin(angle(normal,in_vec))
    sin_theta_output = sin_theta_input * in_n / out_n
    # print(sin_theta_output)
    if sin_theta_output > 1:
        return None
    theta_out = math.asin(sin_theta_output)
    if tan_vec.length() < get_eps():
        out_vec = normal.normalized() * math.cos(theta_out)
    else:
        out_vec = tan_vec.normalized() * sin_theta_output + normal.normalized() * math.cos(theta_out)
    # out_vec = 2 * tan_vec - in_vec
    return HalfLine(out_hl_point,out_vec)

__all__ = ('get_refraction_halfline',)