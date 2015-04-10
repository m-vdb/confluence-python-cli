#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Confluence-py',
    version='1.0.1',
    description='Python Confluence module and command line',
    author='Raymii / Mvdb',
    author_email='mvdb@work4labs.com',
    url='https://github.com/m-vdb/confluence-python',
    packages=['confluence'],
    scripts=["bin/confluence-cli"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
