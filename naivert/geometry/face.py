
class Face(object):
    """
    Face class

    **Input:**

    - cpg: Geometry3D.ConvexPolygen

    - material: Material class

    - is_isolated: a boolean of whether it is a isolated face
    """
    def __init__(self,cpg,material,is_isolated):
        self.cpg = cpg
        self.material = material
        self.is_isolated = is_isolated

__all__ = ('Face',)