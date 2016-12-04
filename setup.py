#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import ast

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def extract_version():
    with open('bilibili/__init__.py', 'rb') as f_version:
        ast_tree = re.search(
            r'__version__ = (.*)',
            f_version.read().decode('utf-8')
        ).group(1)
        if ast_tree is None:
            raise RuntimeError('Cannot find version information')
        return str(ast.literal_eval(ast_tree))

with open('README.rst', 'rb') as f_readme:
    readme = f_readme.read().decode('utf-8')

packages = 'bilibili',

version = extract_version()

setup(
    name='bilibili',
    version=version,
    keywords=['bilibili', 'danmu', 'live'],
    description='I\'m a small script that help you get '
                'bilibili live\'s barrage use aiohttp..',
    long_description=readme,

    author='RayYu03',
    author_email='shiliuhuasheng@gmail.com',
    license='MIT',

    url='https://github.com/RayYu03/bilibili',

    install_requires=['aiohttp','requests','beautifulsoup4'],
    packages=packages,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Information Technology',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],

    entry_points={
        'console_scripts': [
            'bilibili = bilibili.bilibili:main'
        ]
    }
)
