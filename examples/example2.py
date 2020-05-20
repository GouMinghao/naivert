import naivert
from Geometry3D import *
import copy
import itertools
main_scene = naivert.Scene()
main_camera = naivert.Camera(Point(50,-20,50),Point(50,0.01,50),Vector(0,0,20),Vector(20,0,0),'main_camera.png',resolution=(20,20))
point_light = naivert.PointLight(Point(50,100,100),naivert.WHITE)
ambient_light = naivert.AmbientLight([0.0,0.0,10.0])
main_scene.add_camera(main_camera)
main_scene.add_cph(Parallelepiped(origin(),100*x_unit_vector(),100*y_unit_vector(), 100 *z_unit_vector()),naivert.Material.DiffusionMaterial_White_1(),reverse_normal=True)

r = Renderer()
for face in main_scene.face_list:
    r.add((face.cpg,'r',1))

for x,y in itertools.product(range(20),range(20)):
    print(x,y)
    hl = main_camera.primary_halfline(x,y)
    print(hl)
    r.add((Segment(hl.point,copy.deepcopy(hl.point).move(5*hl.vector)),'b',2))
r.show()
# main_scene.render_scene(1)
# main_scene.write_scene()
# print(main_scene)
