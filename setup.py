#!/usr/bin/env python
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

packages = [
'financial_data_utils',
'financial_data_utils.options',
'financial_data_utils.options.yahoo',
'financial_data_utils.libor',
'financial_data_utils.libor.globalrates'
]

requires = ['requests==2.3.0','argparse==1.2.1']

class Tox(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline()
        sys.exit(errno)

setup(name='financial_data_utils',
      version='0.1',
      description='Python Finanical Data Utilities',
      url='https://github.com/creative-quant/finanical-utils',
      license='Apache Software License Version 2.0',
      install_requires=requires,
      packages=packages,
      tests_require=['tox'],
      cmdclass = {'tests': Tox},
     )
