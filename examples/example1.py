import naivert
from Geometry3D import *

main_scene = naivert.Scene()
main_camera = naivert.Camera(Point(50,-50,50),Point(50,0.01,50),Vector(0,0,20),Vector(20,0,0),'main_camera.png',resolution=(5,5))
point_light = naivert.PointLight(Point(50,100,100),naivert.WHITE)
ambient_light = naivert.AmbientLight([0.0,0.0,10.0])
main_scene.add_camera(main_camera)
main_scene.add_light(point_light)
main_scene.add_light(ambient_light)
# main_scene.add_cph(Parallelepiped(origin(),100*x_unit_vector(),100*y_unit_vector(), 100 *z_unit_vector()),naivert.Material.DiffusionMaterial_White_1(),reverse_normal=True)
# main_scene.add_cph(Parallelepiped(Point(30,30,0),10*x_unit_vector(),10*y_unit_vector(), 80 *z_unit_vector()),naivert.Material.DiffusionMaterial_Red_1(),reverse_normal=False)
main_scene.add_cph(Sphere(Point(70,30,40),20,15,5),naivert.Material.Glass(),reverse_normal=False)
main_scene.add_cph(Cone(Point(70,70,0),10,80*z_unit_vector(),n=20),material=naivert.Material.DiffusionMaterial_Green_1(),reverse_normal=False)
# main_scene.add_cph(Cylinder(Point(30,70,0),10,80*z_unit_vector()),material=naivert.Material.SpecularMaterial_White_1(),reverse_normal=False)
r = Renderer()
for face in main_scene.face_list:
    r.add((face.cpg,'r',1))
r.show()
main_scene.render_scene(1)
main_scene.write_scene()
# print(main_scene)
