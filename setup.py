
from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
name='aviation_mro',
title='Aviation MRO',	
version='1.0.0',
description='Aviation maintenance and inventory for parts',
long_description=long_description,
long_description_content_type='text/markdown',
author='Ed Harrison',
author_email='ed@turbinetech.aero',
license='MIT',
packages=find_packages(),
zip_safe=False,
include_package_data=True,
install_requires=['frappe'],
classifiers=[
   'Framework :: Frappe',
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3'
    ]
    )