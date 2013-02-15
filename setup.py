# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-xanax-bootstrap',
    version='0.1.0',
    author='Vishnevski Alexey',
    author_email='vishnevski.a@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://pypi.python.org/pypi/django-xanax-bootstrap/',
    license='LICENSE',
    description='Django-xanax-bootstrap is a simple integration django-xanax and django-admintools-bootstrap.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.4.0",
        ],
)
