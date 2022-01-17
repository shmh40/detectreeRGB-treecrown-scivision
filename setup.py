#!/usr/bin/env python
from setuptools import find_packages, setup

try:
    import torch
    import torchvision

    print(torch.__version__)
    print(torchvision.__version__)
except ImportError:
    raise Exception(
        """
You must install PyTorch and torchvision prior to installing:
!pip -q install torch==1.8.0
!pip -q install torchvision==0.9.0

For more information:
    https://pytorch.org/get-started/locally/
    """
    )

requirements = []
with open("requirements.txt") as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name="scivision_treecrown_plugin",
    version="0.0.1",
    description="scivision treecrown plugin",
    author="Alejandro Coca-Castro",
    author_email="acocac@turing.ac.uk",
    url="https://github.com/acocac/scivision-treecrown-plugin",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
)
