#!/usr/bin/env python

#===================================================================================================
# Imports
#===================================================================================================
try:
  # setuptools is used to build wheels. Fallback to distutils if it isn't available.
  from setuptools import setup
except ImportError:
  from distutils.core import setup

from vmpooler_client.version import version

#===================================================================================================
# Main
#===================================================================================================
setup(name='vmpooler-client',
       version=version,
       description='Manage resources in the vmpooler service from the command-line.',
       author='Ryan Gard',
       author_email='ryan.gard@puppetlabs.com',
       url='https://github.com/puppetlabs/vmpooler-client',
       packages=['vmpooler_client', 'vmpooler_client.commands'],
       scripts=['vmpooler_client_app.py']
     )
