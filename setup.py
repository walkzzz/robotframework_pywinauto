#!/usr/bin/env python

import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: Microsoft :: Windows
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3.13
Programming Language :: Python :: 3.14
Programming Language :: Python :: 3 :: Only
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()
with open(join(CURDIR, 'src', 'pywinautoLibrary', '__init__.py')) as f:
    VERSION = re.search('\n__version__ = "(.*)"', f.read()).group(1)
with open(join(CURDIR, 'README.rst')) as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name             = 'robotframework-pywinauto',
    version          = VERSION,
    description      = 'Windows desktop application testing library for Robot Framework',
    long_description = DESCRIPTION,
    author           = 'Robot Framework Foundation',
    author_email     = 'robotframework@gmail.com',
    url              = 'https://github.com/robotframework/robotframework-pywinauto',
    license          = 'Apache License 2.0',
    keywords         = 'robotframework testing testautomation pywinauto windows desktop',
    platforms        = 'Windows',
    classifiers      = CLASSIFIERS,
    python_requires  = '>=3.8',
    install_requires = REQUIREMENTS,
    package_dir      = {'': 'src'},
    packages         = find_packages('src'),
    package_data     ={
        'pywinautoLibrary':
            ['*.pyi']
    }
)