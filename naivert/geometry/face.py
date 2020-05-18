
class Face(object):
    def __init__(self,cpg,material,is_isolated):
        self.cpg = cpg
        self.material = material
        self.is_isolated = is_isolated

__all__ = ('Face',)