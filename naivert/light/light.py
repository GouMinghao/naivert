from Geometry3D import *
import copy

class PointLight(object):
    '''
    Point light source class

    ** Input: **

    - pos: Geometry3D.Point

    - rgb: list of rgb light strength
    '''
    def __init__(self,pos,rgb):
        self.pos = pos
        self.rgb = copy.deepcopy(rgb)

__all__ = ('PointLight',)