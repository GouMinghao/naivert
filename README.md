# naivert

naivert is an pure Python implementation of ray tracing algorithm using Phong illumination model.  
For geometry calculation, naivert uses the library of [Geometry3D](https://github.com/GouMinghao/Geometry3D).
Basic materials and light sources are given in the configuration file. You can also define the material and light source by yourself.
You may refer to the examples and documentation of Geometry3D to get to know how to use naivert.

## Requirements

numpy, Geometry3D, matplotlib and opencv-python

## Installation

```bash
pip install naivert
```

## Examples
Run .py files under examples folder.  
For example:
```bash
python example3.py
```
![sample3](sample3.png)

```bash
python example4.py
```
![sample3](sample4.png)

```bash
python example5.py
```
![sample3](sample5.png)

Note that the calculation may be very slow. You can modify the resolution of the image to reduce the time cost.

## Documentations
[HTML](https://naivert.readthedocs.io/en/latest/)  
[PDF](https://naivert.readthedocs.io/_/downloads/en/latest/pdf/)