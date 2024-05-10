# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import setup, find_packages


setup(
    name='sitralib',
    version='1.1.82',
    packages=find_packages( exclude=['test'] ),
    author='Agustin Bouillet',
    author_email='agustin.bouillet@gmail.com',
    url='http://www.bouillet.com.ar/',
    description='Libreria SITRA',
    # long_description = """Really long text here."""
)