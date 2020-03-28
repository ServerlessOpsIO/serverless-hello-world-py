#!/usr/bin/env python

import io
import re
import os
from setuptools import setup, find_packages

setup(
    name='common',
    version='0.0.1',
    description='serverless-hello-world-py Service Common Code',
    author='Tom McLaughlin',
    author_email='tom@serverlessops.io',
    license='Apache License 2.0',
    packages=find_packages(exclude=['tests.*', 'tests']),
    keywords="serverless-hello-world-py Service",
    python_requires='>=3.8.*',
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Environment :: Other Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ]
)

