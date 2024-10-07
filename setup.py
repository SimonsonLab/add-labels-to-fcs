#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(name='add_labels_to_fcs',
      version='0.3.1',
      description='Package for adding columns of data to FCS files as additional channels',
      author='Paul D. Simonson',
      url='https://github.com/SimonsonLab/add-labels-to-fcs',
      packages=find_packages(),
      install_requires=['pandas>=2.2', 'openpyxl>=3.1', 'numpy>=1.26', 'flowkit>=1.1'],
      entry_points={
          "console_scripts":[
              "add-labels-to-fcs-hello = add_labels_to_fcs:hello",
              "add-labels-as-grid-to-fcs = add_labels_to_fcs.add_labels:add_labels_as_grid_to_FCS_CLI",
              "add-labels-to-fcs = add_labels_to_fcs.add_labels:add_labels_to_FCS_CLI",
          ]
      },
      long_description_content_type="text/markdown",
      long_description=description,
     )
