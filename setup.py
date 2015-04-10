#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Confluence-py',
    version='1.0',
    description='Python Confluence module and command line',
    author='Raymii / Mvdb',
    author_email='mvdb@work4labs.com',
    url='https://github.com/m-vdb/confluence-python',
    packages=['confluence'],
    scripts=["bin/confluence-cli"]
)
