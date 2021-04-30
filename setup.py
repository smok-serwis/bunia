#!/usr/bin/env python
# coding=UTF-8
from setuptools import setup

setup(name='bunia',
      version='1.0',
      description='Write commands that use multiple interfaes',
      author='Piotr Maślanka',
      author_email='pmaslanka@smok.co',
      url='https://github.com/smok-serwis/bunia',
      download_url='https://github.com/smok-serwis/bunia/archive/v1.0.zip',
      keywords=['arguments', 'argparse', 'html', 'console'],
      platforms=['any'],
      packages=['bunia',
                'bunia.runner',
                'bunia.api',
                'bunia.output',
                ],
      requires=[
          'six'
      ],
      tests_require=[
          "nose"
      ],
      test_suite='nose.collector',
      license='MIT License',
      long_description='''This is an interface for writing commands that can use multiple interfaces, ie. you can launch
it from shell, Web, SMS, etc.

A device-independent output and input is presented.''',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Operating System :: OS Independent'
      ]
)
