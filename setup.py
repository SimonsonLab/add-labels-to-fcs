#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(name='add_labels_to_fcs',
      version='0.2',
      description='Package for adding columns of data to FCS files as additional channels',
      author='Paul D. Simonson',
      url='https://github.com/SimonsonLab/add-labels-to-fcs',
      packages=find_packages(),
      install_requires=[pandas, openpyxl, numpy, flowkit],
      entry_points={
          "console_scripts":[
              "add-labels-to-fcs-hello = add_labels_to_fcs:hello",
          ]
      },
      long_description_content_type="text/markdown",
      long_description=description,
     )