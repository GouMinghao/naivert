from Geometry3D import Vector,orthogonal
import numpy as np
import cv2
import itertools
import copy

from ..geometry.inter_halfline_face_list import inter_halfline_face_list
from ..geometry.get_refraction_halfline import get_refraction_halfline
from ..geometry.get_reflection_halfline import get_reflection_halfline
from ..utils.constant import get_rt_max_depth,NO_LOSS

class Camera(object):
    '''
    Camera class.

    ** Input: **

    - focus_point: a Geometry3D.Point of the focus point

    - main_point: a Geometry3D.Point of the main point on the main plane

    - x_vec: a Geometry3D.Vector of the x_vector of the camera

    - y_vec: a Geometry3D.Vector of the y_vector of the camera

    - resolution: a tuple of int of the resolution
    '''

    def __init__(self,focus_point,main_point,x_vec,y_vec,image_path=None,resolution=(640,480)):
        self.focus_point = focus_point
        self.main_point = main_point
        self.x_vec = x_vec
        self.y_vec = y_vec
        self.resolution = resolution
        self.z_vec = Vector(focus_point,main_point)
        self.image = np.zeros((resolution[0],resolution[1],3),dtype=np.float32)
        self.image_path = image_path
        if not orthogonal(self.x_vec,self.y_vec):
            raise ValueError('x_vec and y_vec are not orthogonal')
        if not orthogonal(self.x_vec,self.z_vec):
            raise ValueError('x_vec and z_vec are not orthogonal')
        if not orthogonal(self.y_vec,self.z_vec):
            raise ValueError('y_vec and z_vec are not orthogonal')

    def primary_halfline(self,x,y):
        '''
        **Input:**

        - x: int of the index of the array.

        - y: int of the index of the array.
    'Material',
        **Output:**

        - Geometry3D.HalfLine of the primary ray of the (x,y) pixel.
        
        ** Illustration: **

        - The figure is given in the root folder/camera.png
        ''' 
        # needs to be implemented.

    def set_image_path(self,image_path):
        self.image_path = image_path
    
    def write_image(self):
        import cv2
        if self.image_path is None:
            raise ValueError('Image path not set for this camera')
        cv2.imwrite(self.image_path,self.image)

    def unify_intensity(self):
        self.image = self.image / (max(self.image))

def ren_camera(camera,face_list,light_list):
    '''
    ** Input: **
    
    - camera: Camera of the camera that want to render

    - face_list: a list of Faces of a scene

    - light_list: a list of Light of the scene
    '''
    for x,y in itertools.product(range(camera.resolution[0]),range(camera.resolition[1])):
        primary_halfline = camera.primary_halfline(x,y)
        ray_list = []
        trace_ray(primary_halfline,[],ray_list,face_list,depth = get_rt_max_depth(),n = 1)
        camera.image[x][y] = cal_ray(ray_list)
    camera.unify_intensity()


def trace_ray(halfline,trace_list,ray_list,face_list,depth,n=1):
    '''
    **Input:**
    
    - halfline: Geometry3D.HalfLine of the input HalfLine

    - trace_list: a list of the current path of the ray now

    - ray_list: a list of trace list which will be used to calculate the intersity of light

    - face_list: a list of Faces of the scene

    - depth: the transformation depth remained

    - n: a float of the refraction rate of the input material
    '''
    if depth == 0:
        return
    inter_point,d,face = inter_halfline_face_list(halfline,face_list)
    if inter_point is None:
        return
    if n > 1: # when the ray come out of a transparent 
        refraction_halfline = get_refraction_halfline(halfline,n,1,face.cpg)
        # only refraction ray
        trace_ray(refraction_halfline,copy.deepcopy(trace_list).append(d).append(NO_LOSS),ray_list,face_list,depth = depth-1,n = 1)
    else: # n == 1
        # refraction ray
        if (face.material.f_refract == np.zeros(3)).all(): # there should be refraction of the material
            refraction_halfline = get_refraction_halfline(halfline,1,face.material.n,face.cpg)
            trace_ray(refraction_halfline,copy.deepcopy(trace_list).append(d).append(face.material.f_refract),ray_list,face_list,depth = depth - 1,n = face.material.n)
        # reflection ray
        reflection_halfline = get_reflection_halfline(halfline,face.cpg)
        trace_ray(reflection_halfline,copy.deepcopy(trace_list).append(d).append(face.material.f_reflect),ray_list,face_list,depth = depth - 1,n = face.material.n)
        # light
            

def cal_ray(ray_list):
    return np.array([0,0,0],dtype=np.uint8)
    # needs to be implemented.

__all__=('Camera','ren_camera')