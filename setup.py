#!/usr/bin/env python
#coding=UTF-8
from distutils.core import setup

setup(name='bunia',
      version='0.0a',
      description=u'Write commands that use multiple interfaes',
      author=u'DMS Serwis s.c.',
      author_email='piotrm@smok.co',
      url='https://github.com/smok-serwis/bunia',
      download_url='https://github.com/smok-serwis/coolamqp/archive/bunia.zip',
      keywords=['arguments', 'argparse', 'html', 'console'],
      packages=['bunia',
                'bunia.runner',
                'bunia.api',
                'bunia.discovery',
                'bunia.outputs',
                ],
      license='MIT License',
      long_description=u'''This is an interface for writing commands that can use multiple interfaces, ie. you can launch
it from shell, Web, SMS, etc.

A device-independent output and input is presented.'''
)