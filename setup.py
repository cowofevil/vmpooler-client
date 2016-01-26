#!/usr/bin/env python

#===================================================================================================
# Imports
#===================================================================================================
from distutils.core import setup

#===================================================================================================
# Main
#===================================================================================================
setup(name='vmpooler-client',
       version='2.4.2',
       description='Manage resources in the vmpooler service from the command-line.',
       author='Ryan Gard',
       author_email='ryan.gard@puppetlabs.com',
       url='https://github.com/puppetlabs/vmpooler-client',
       packages=['lib', 'lib.commands'],
       scripts=['vmpooler_client.py']
     )
