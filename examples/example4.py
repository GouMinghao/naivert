import naivert
from Geometry3D import *
from math import sqrt

main_scene = naivert.Scene()
main_camera = naivert.Camera(Point(400,-300,400),Point(385,-285,385),10 * Vector(-1 /sqrt(6),1/sqrt(6),2/sqrt(6)),10*Vector(1/sqrt(2),1/sqrt(2),0),'main_camera.png',resolution=(100,100))
point_light2 = naivert.PointLight(Point(200,50,200),[4.0,4.0,4.0])
point_light = naivert.PointLight(Point(50,100,200),[5.0,5.0,5.0])
main_scene.add_camera(main_camera)
main_scene.add_light(point_light)
main_scene.add_light(point_light2)

main_scene.add_floor(-50,200,-50,200)

main_scene.add_cph(Sphere(Point(0,0,0),15,30,15),naivert.Material.DiffusionMaterial_White_1(),reverse_normal=False)
main_scene.add_cph(Sphere(Point(100,0,0),15,30,15),naivert.Material.DiffusionMaterial_Green_1(),reverse_normal=False)
main_scene.add_cph(Sphere(Point(100,100,0),15,30,15),naivert.Material.DiffusionMaterial_Red_1(),reverse_normal=False)
main_scene.add_cph(Sphere(Point(0,100,0),15,30,15),naivert.Material.DiffusionMaterial_Blue_1(),reverse_normal=False)
main_scene.render_scene(56)
main_scene.write_scene()
