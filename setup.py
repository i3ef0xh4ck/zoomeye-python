#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
* Filename: setup.py
* Description:
* Time: 2020.11.27
* Author: liuf5
*/
"""
from setuptools import setup

setup(
    name='zoomeye',
    version='0.3',
    description='Python library and command-line utility for ZoomEye (https://www.zoomeye.org/doc)',
    long_description=open('README.md').read(),
    long_description_content_type='text/x-rst',
    author='404 Team@Knownsec',
    packages=['zoomeye'],
    entry_points={'console_scripts': ['zoomeye=zoomeye.cli:main']},
    install_requires="DEPENDENCIES",
    keywords=['security tool', 'zoomeye'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
