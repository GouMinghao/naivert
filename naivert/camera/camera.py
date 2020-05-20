from Geometry3D import Vector, orthogonal, distance, HalfLine, Renderer, Segment
import numpy as np
import cv2
import itertools
import copy
import math
from multiprocessing import Pool

from ..geometry.inter_halfline_face_list import inter_halfline_face_list
from ..geometry.get_refraction_halfline import get_refraction_halfline
from ..geometry.get_reflection_halfline import get_reflection_halfline
from ..utils.constant import get_rt_max_depth,NO_LOSS
from ..light import AmbientLight, PointLight

class Camera(object):
    """
    Camera class.

    **Input:**

    - focus_point: a Geometry3D.Point of the focus point

    - main_point: a Geometry3D.Point of the main point on the main plane

    - x_vec: a Geometry3D.Vector of the x_vector of the camera

    - y_vec: a Geometry3D.Vector of the y_vector of the camera

    - resolution: a tuple of int of the resolution
    """

    def __init__(self,focus_point,main_point,x_vec,y_vec,image_path=None,resolution=(640,480)):
        self.focus_point = focus_point
        self.main_point = main_point
        self.x_vec = x_vec
        self.y_vec = y_vec
        self.resolution = resolution
        self.z_vec = Vector(focus_point,main_point)
        self.image = np.zeros((resolution[1],resolution[0],3),dtype=np.float32)
        self.image_path = image_path
        if not orthogonal(self.x_vec,self.y_vec):
            raise ValueError('x_vec and y_vec are not orthogonal')
        if not orthogonal(self.x_vec,self.z_vec):
            raise ValueError('x_vec and z_vec are not orthogonal')
        if not orthogonal(self.y_vec,self.z_vec):
            raise ValueError('y_vec and z_vec are not orthogonal')

    def primary_halfline(self,x,y):
        """
        **Input:**

        - x: int of the index of the array.

        - y: int of the index of the array.

        **Output:**

        - Geometry3D.HalfLine of the primary ray of the (x,y) pixel.
        
        **Illustration:**

        - The figure is given in the root folder/camera.png
        """
        width = self.resolution[1]
        height = self.resolution[0]
        x_step_vec = -self.x_vec * (1/width) # be careful here, don't confuse the x and y
        y_step_vec = self.y_vec * (1/height) # be careful here, don't confuse the x and y
        p = copy.deepcopy(self.main_point).move(x_step_vec * (-width / 2 + x + 0.5)).move(y_step_vec * (-height / 2 + y + 0.5))
        return HalfLine(p,Vector(self.focus_point,p))

    def set_image_path(self,image_path):
        """
        **Input:**
        image_path: the string of the path of the image that will be saved
        """
        self.image_path = image_path
    
    def write_image(self):
        """
        **Function:**
        
        - Write the image to the file
        """ 
        import cv2
        if self.image_path is None:
            raise ValueError('Image path not set for this camera')
        cv2.imwrite(self.image_path,(self.image * 255.0).astype(np.uint8))

    def unify_intensity(self):
        """
        **Function:**
        
        - Unify the intensity of the image to [0,1]
        """
        self.image = cv2.medianBlur(self.image,3)
        print(self.image)
        self.image = self.image / np.max(self.image)

def ren_camera_wrapper(it):
    (x,y,camera,face_list,light_list) = it
    print('rendering pixel x={}, y={}'.format(x,y))
    primary_halfline = camera.primary_halfline(x,y)
    ray_list = []
    trace_ray(primary_halfline,[],ray_list,face_list,[],light_list,depth = get_rt_max_depth(),current_face = None,n = 1)
    return cal_ray(ray_list)

def get_iter(camera,face_list,light_list):
    for x,y in itertools.product(range(camera.resolution[1]),range(camera.resolution[0])):
        yield (x,y,camera,face_list,light_list)

def ren_camera(camera,face_list,light_list,num_proc = 1):
    """
    **Input:**
    
    - camera: Camera of the camera that want to render

    - face_list: a list of Faces of a scene

    - light_list: a list of Light of the scene
    """
    if num_proc == 1:
        for x,y in itertools.product(range(camera.resolution[1]),range(camera.resolution[0])):
            print('rendering pixel x={}, y={}'.format(x,y))
            primary_halfline = camera.primary_halfline(x,y)
            ray_list = []
            trace_ray(primary_halfline,[],ray_list,face_list,[],light_list,depth = get_rt_max_depth(),current_face = None,n = 1)
            # for ray in ray_list:
            #     print(ray)
            camera.image[x][y] = cal_ray(ray_list)
    else:
        p = Pool(processes=num_proc)
        res = p.map(ren_camera_wrapper,get_iter(camera,face_list,light_list))
        print(res)
        i=0
        for x,y in itertools.product(range(camera.resolution[1]),range(camera.resolution[0])):
            camera.image[x][y] = res[i]
            i+=1
        p.close()
        p.join()
    camera.unify_intensity()


def trace_ray(halfline,trace_list,ray_list,face_list,point_list,light_list,depth,current_face,n=1):
    """
    **Input:**
    
    - halfline: Geometry3D.HalfLine of the input HalfLine

    - trace_list: a list of the current path of the ray now

    - ray_list: a list of trace list which will be used to calculate the intersity of light

    - face_list: a list of Faces of the scene

    - depth: the transformation depth remained

    - n: a float of the refraction rate of the input material
    """
    
    if depth == 0:
        return
    inter_point,d,face = inter_halfline_face_list(halfline,face_list,current_face=current_face) 
    if inter_point is None:
        return
    # print('call trace_ray with trace_list={},d={},point={},cpg={}\n'.format(trace_list,d,inter_point,face.cpg))
    if n > 1: # when the ray come out of a transparent 
        refraction_halfline = get_refraction_halfline(halfline,n,1,face.cpg)
        if refraction_halfline is not None:
        # only refraction ray
            trace_ray(
                halfline = refraction_halfline,
                trace_list = copy.deepcopy(trace_list)+[d,NO_LOSS],
                ray_list = ray_list,
                face_list = face_list,
                point_list = copy.deepcopy(point_list)+[inter_point],
                light_list = light_list,
                depth = depth-1,
                current_face = face,
                n = 1
            )
    else: # n == 1
        # refraction ray
        if not (face.material.f_refract == np.zeros(3)).all(): # there should be refraction of the material
            refraction_halfline = get_refraction_halfline(halfline,1,face.material.n,face.cpg)
            if refraction_halfline is not None:
                trace_ray(
                    halfline = refraction_halfline,
                    trace_list = copy.deepcopy(trace_list)+[d,face.material.f_refract],
                    ray_list = ray_list,
                    face_list = face_list,
                    point_list = copy.deepcopy(point_list)+[inter_point],
                    light_list = light_list,
                    depth = depth - 1,
                    current_face = face,
                    n = face.material.n
                )      
        # reflection ray
        reflection_halfline = get_reflection_halfline(halfline,face.cpg)
        trace_ray(
            halfline = reflection_halfline,
            trace_list = copy.deepcopy(trace_list)+[d,face.material.f_reflect],
            ray_list = ray_list,
            face_list = face_list,
            point_list = copy.deepcopy(point_list)+[inter_point],
            light_list = light_list,
            depth = depth - 1,
            current_face = face,
            n = face.material.n
        )
        # light
        for light in light_list:
            if isinstance(light,AmbientLight):
                # print('\033[0;32mpts list:\033[0m{}'.format(point_list))
                ray_list.append(copy.deepcopy(trace_list)+[d,face.material.ka,light])
            elif isinstance(light,PointLight):
                # print('\033[0;32mpts list:\033[0m{}'.format(point_list))


                # r = Renderer()
                # for face in face_list:
                #     r.add((face.cpg,'r',1))
                # for i in range(len(point_list) - 1):
                #     r.add((Segment(point_list[i],point_list[i+1]),'b',2))
                # r.show()

                
                light_i,light_d,light_f=inter_halfline_face_list(HalfLine(inter_point,light.pos),face_list,current_face=face) 
                if not light_i == light.pos:
                    continue
                L_vec = Vector(inter_point,light.pos).normalized()
                N_vec = face.cpg.plane.n.normalized()
                V_vec = halfline.vector.normalized()
                R_vec = reflection_halfline.vector.normalized()
                H_vec = 0.5*(V_vec + L_vec).normalized()
                i_s = np.zeros(3,dtype = np.float32)
                for i in range(3):
                    i_s[i] = face.material.ks[i] * math.pow(R_vec * V_vec,face.material.alpha)
                i_d = face.material.kd * (L_vec * N_vec)
                d_light = distance(inter_point,light.pos)
                ray_list.append(copy.deepcopy(trace_list)+[d,i_s+ i_d,d_light,light])
            else:
                raise TypeError('Unknown Light Type:{}'.format(type(light)))

def cal_ray(ray_list):
    """
    **Input:**

    - ray_list: a list of ray list

    **Output:**

    -  the sum intensity of all the rays
    """
    intensity = np.zeros(3,dtype = np.float32)
    
    for ray in ray_list:
        
        total_d = 0
        ray_intensity = np.array(ray[-1].rgb)
        for k in reversed(ray[:-1]):
            if isinstance(k,np.ndarray):
                ray_intensity *= k
            else: #distance
                if total_d == 0:
                    if k < 1e-5:
                        k = 0.01
                    ray_intensity *= 1 / math.pow(k,2)
                    total_d = k 
                else:
                    ray_intensity *= math.pow(total_d,2) / math.pow(total_d + k,2)
                    total_d += k
        intensity += ray_intensity
        print('\033[0;34mRAY:\033[0m{},result=:{}'.format(ray,ray_intensity))
    return intensity
    

__all__=('Camera','ren_camera')
