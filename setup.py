# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def read(name):
    with open(name, "r") as fd:
        return fd.read()

setup(
        name="naivert",
        version="0.0.1",

        description="A Naive Ray Tracing Implementation",
        long_description=read("README.md"),

        url="https://github.com/GouMinghao/naive-rt",

        author="Minghao Gou",
        author_email="gouminghao@gmail.com",

        license="GPL",

        packages=find_packages(),
    
        classifiers=[
            "Intended Audience :: Developers",
            "Intended Audience :: Education",

            "Topic :: Education",
            "Topic :: Scientific/Engineering :: Mathematics",

            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",

            "Programming Language :: Python :: 3",
        ],

        keywords="ray tracing",

        install_requires=['numpy', 'Geometry3D==0.2.0']
)
