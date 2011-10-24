#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pythonicus',
    version='0.1',
    description='Natural Language Processor web server',
    author='Diego Rubin',
    author_eamil='rubin.diego@gmail.com',
    url='http://diegorubin.com/projects/pythonicus',

    include_package_data = True,

    packages=find_packages()
)

