#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

install_requires=[]

dependency_links=[
    'http://github.com/savoirfairelinux/num2words/tarball/master#egg=num2words',
]

setup(
    name='literumi',
    url='https://github.com/MarkusShepherd/literumi',
    version='0.0.1',
    description='spells numbers',
    packages=['literumi'],
    install_requires=install_requires,
    dependency_links=dependency_links,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    long_description='''
    spells numbers
    '''
)
