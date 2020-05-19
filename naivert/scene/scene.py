from ..camera.camera import Camera,ren_camera
from ..material.material import Material
from ..light.light import PointLight
from ..geometry.face import Face

import itertools

class Scene(object):
    '''
    Scene Class
    '''
    def __init__(self):
        self.face_list = []
        self.light_list = []
        self.camera_list = []
        
    def cpgs(self):
        '''
        iterator of all the cpg in the face list.
        '''
        for face in self.face_list:
            yield face.cpg
    
    def add_cph(self,cph,material,reverse_normal = False):
        '''
        **Input:**

        - cph: Geometry3D.ConvexPolyhedron of the cph that is wanted to be added.

        - material: Material of the material.

        - reverse_normal: boolean of whether reverse the normal of tha cpgs.
        '''
        for cpg in cph.convex_polygens:
            if reverse_normal:
                cpg = -cpg
            self.face_list.append(Face(cpg = cpg,material = material,is_isolated = False))

    def add_cpg(self,cpg,material):
        '''
        **Input:**

        - cpg: Geometry3D.ConvexPolygen of the cpg that is wanted to be added.

        - material: Material of the material.
        '''
        self.face_list.append(Face(cpg = cpg,material = material, is_isolated = True))

    def add_light(self,light):
        '''
        **Input:**

        - a Light that is to be added.
        '''
        self.light_list.append(light)

    def add_camera(self,camera):
        '''
        **Input:**
        
        -  a Camera that is to be added.
        '''
        self.camera_list.append(camera)

    def render_scene(self):
        '''
        render all the camera images under the scene.
        '''
        for camera in self.camera_list:
            ren_camera(camera,self.face_list,self.light_list)

    def write_scene(self):
        '''
        write all the camera images to the file.
        '''        
        for camera in self.camera_list:
            camera.write_image()

    def __repr__(self):
        return 'Scene contains {} light, {} camera and {} faces'.format(len(self.light_list),len(self.camera_list),len(self.face_list))

