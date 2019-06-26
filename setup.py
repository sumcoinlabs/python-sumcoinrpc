#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-sumcoinrpc',
    version='1.0',
    description='Enhanced version of python-jsonrpc for use with Sumcoin',
    long_description=open('README.rst').read(),
    author='Sumtoshi',
    author_email='<support@sumcoinindex.com>',
    maintainer='Sumcoin Index',
    maintainer_email='<support@sumcoinindex.com>',
    url='http://www.github.com/sumcoinlabs/python-sumcoinrpc',
    packages=['sumcoinrpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)
