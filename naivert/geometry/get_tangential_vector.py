
from Geometry3D import Vector,angle,get_eps
def get_tangential_vector(in_vec,n):
    """
    **Input:**

    - in_vec: Geometry3D.Vector
    
    - n: Geometry3D.Vector and n * in_vec > 0

    **Output:**

    - tan_vec: Geometry3D.Vector of the tangential vector
    """
    assert in_vec * n > get_eps()
    norm_n = n.normalized()
    norm_length = in_vec * norm_n
    tan_vec = in_vec - norm_n * norm_length
    return tan_vec 

__all__ = ('get_tangential_vector',)