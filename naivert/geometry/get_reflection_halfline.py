from Geometry3D import HalfLine, Point

def get_reflection_halfline(in_hl,in_n,out_n,cpg):
    '''
    ** Input: **

    - in_hl: Geometry3D.HalfLine of input half line.

    - in_n: float of the inner material refraction rate

    - out_n: float of the outer material refraction rate

    - cpg: Geometry3D.ConvexPolygen of the intersection convex polygen

    ** Output: **

    - out_hl: Geometry3D.HalfLine of output half line.
    '''
    out_hl_point = intersection(in_hl,cpg)
    if out_hl_point is None:
        return None:
    if not isinstance(out_hl_point,Point):
        return None:
    