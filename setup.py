#!/usr/bin/env python
from setuptools import find_packages, setup

requirements = []
with open("requirements.txt") as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name="detectreeRGB_treecrown_scivision",
    version="0.0.1",
    description="detectreeRGB_treecrown_scivision",
    author="Sebastian Hickman",
    author_email="shmh4@cam.ac.uk",
    url="https://github.com/acocac/detectreeRGB-treecrown-scivision",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
)
