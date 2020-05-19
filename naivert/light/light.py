from Geometry3D import *
import copy
class Light(object):
    '''
    A base light class
    '''
    pass

class PointLight(Light):
    '''
    Point light source class

    ** Input: **

    - pos: Geometry3D.Point

    - rgb: list of rgb light strength
    '''
    def __init__(self,pos,rgb):
        self.pos = pos
        self.rgb = copy.deepcopy(rgb)

class AmbientLight(Light):
    '''
    Ambient light source class

    ** Input: **

    - rgb: list of rgb light strength
    '''
    def __init__(self,rgb):
        self.rgb = copy.deepcopy(rgb)

__all__ = ('Light','PointLight','AmbientLight')