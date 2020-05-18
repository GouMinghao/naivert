from Geometry3D import Vector,orthogonal
import numpy as np
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
        self.image = np.zeros((3,resolution[0],resolution[1]))
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

        - x and y are the numpy array indexes.

        **Output:**

        - Geometry3D.HalfLine of the primary ray of the (x,y) pixel.
        
        ** Illustration: **

        - The figure is given in the root folder/camera.png
        ''' 


    def set_image_path(self,image_path):
        self.image_path = image_path
    
    def write_image(self):
        import cv2
        if self.image_path is None:
            raise ValueError('Image path not set for this camera')
        cv2.imwrite(self.image_path,self.image)

__all__=('Camera',)