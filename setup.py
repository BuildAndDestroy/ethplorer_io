#!/usr/bin/env python
"""
	To install, run:
	sudo pip install .
	If upgrading, run:
	sudo pip install --upgrade .
"""

from setuptools import setup

__version__ = '1.0dev'
packages = ['ethplorer']
commands = ['ethplorer_transaction = ethplorer.user_interact:main']
__author__ = 'Mitch O\'Donnell'

setup(
	name 				= 'Ethplorer API',
	version 			= __version__,
	description 		= 'API call to api.ethplorer.io to pull transaction queries.',
	author 				= __author__,
	author_email 		= 'devreap1@gmail.com',
	packages 			= packages,
	url 				= '',
	license 			= open('LICENSE').read(),
	install_requires 	= ['prettytable'],
	entry_points 		= {'console_scripts': commands},
	prefix 				= '/opt/Ethplorer_API',
	long_description 	= open('README.md').read()
)
