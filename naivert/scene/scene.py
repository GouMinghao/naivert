from ..camera.camera import Camera,ren_camera
from ..material.material import Material
from ..light.light import PointLight
from ..geometry.face import Face

import itertools

# def ren_camera(camera,face_list,light_list):
#     for x,y in itertools.product(range(camera.resolution[0]),range(camera.resolition[1])):
#         ren_ray

class Scene(object):
    def __init__(self):
        self.face_list = []
        self.light_list = []
        self.camera_list = []
        
    def cpgs(self):
        for face in self.face_list:
            yield face.cpg
    
    def add_cph(self,cph,material,reverse_normal = False):
        for cpg in cph.convex_polygens:
            if reverse_normal:
                cpg = -cpg
            self.face_list.append(Face(cpg = cpg,material = material,is_isolated = False))

    def add_cpg(self,cpg,material):
        self.face_list.append(Face(cpg = cpg,material = material, is_isolated = True))

    def add_light(self,light):
        self.light_list.append(light)

    def add_camera(self,camera):
        self.camera_list.append(camera)

    def render_scene(self):
        for camera in self.camera_list:
            ren_camera(camera,self.face_list,self.light_list)

        

