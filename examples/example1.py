import naivert
from Geometry3D import *
from math import sqrt

main_scene = naivert.Scene()
main_camera = naivert.Camera(Point(300,-200,300),Point(280,-180,280),10 * Vector(-1 /sqrt(6),1/sqrt(6),2/sqrt(6)),10*Vector(1/sqrt(2),1/sqrt(2),0),'main_camera.png',resolution=(200,200))
# main_camera = naivert.Camera(Point(70,-100,50),Point(70,-50,50),Vector(0,0,40),Vector(40,0,0),'main_camera.png',resolution=(100,100))
point_light = naivert.PointLight(Point(50,100,200),[5.0,5.0,5.0])
point_light2 = naivert.PointLight(Point(200,50,200),[4.0,4.0,4.0])
ambient_light = naivert.AmbientLight([3.0,3.0,3.0])
main_scene.add_camera(main_camera)
main_scene.add_light(point_light)
main_scene.add_light(point_light2)
main_scene.add_light(ambient_light)
# main_scene.add_cph(Parallelepiped(origin(),100*x_unit_vector(),100*y_unit_vector(), 100 *z_unit_vector()),naivert.Material.DiffusionMaterial_White_1(),reverse_normal=True)
main_scene.add_cph(Parallelepiped(Point(-50,-50,0),200*x_unit_vector(),200*y_unit_vector(), -10*z_unit_vector()),naivert.Material.DiffusionMaterial_White_1(),reverse_normal=False)
main_scene.add_cph(Parallelepiped(Point(60,20,0),20*x_unit_vector(),20*y_unit_vector(), 150*z_unit_vector()),naivert.Material.Glass(),reverse_normal=False)
main_scene.add_cph(Parallelepiped(Point(10,10,20),20*x_unit_vector(),20*y_unit_vector(), 50 *z_unit_vector()),naivert.Material.DiffusionMaterial_Red_1(),reverse_normal=False)
main_scene.add_cph(Sphere(Point(70,70,40),20,40,20),naivert.Material.SpecularMaterial_White_1(),reverse_normal=False)
main_scene.add_cph(Sphere(Point(100,50,0),20,40,20),naivert.Material.SpecularMaterial_White_1(),reverse_normal=False)
main_scene.add_cph(Cone(Point(30,130,0),10,80*z_unit_vector(),n=20),material=naivert.Material.DiffusionMaterial_Green_1(),reverse_normal=False)
main_scene.add_cph(Cylinder(Point(30,70,0),15,80*z_unit_vector(),n=40),material=naivert.Material.SpecularMaterial_White_1(),reverse_normal=False)
r = Renderer()
for face in main_scene.face_list:
    r.add((face.cpg,'r',1))
r.show()
main_scene.render_scene(56)
main_scene.write_scene()
# print(main_scene)
