#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
tests_require = [
    "nose",

]

def run_setup():
    setup(name='CSVToWiki',
          version='1.0',
          description='Converts a csv into a wiki table',
          author='Joseph Dunaravich',
          author_email='dunarav@amazon.com',
          url='https://www.amazon.com/',
          packages=['csvtowiki'],
          package_dir={"csvtowiki": "csvtowiki"},
          install_requires=[
              "argparse"
          ],
         )


run_setup()
