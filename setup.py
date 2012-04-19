# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='nosegrowl',
    version='0.0.1',
    description='Simplified, all Pythonic nosegrowl - Growl notifications for Nosetests.',
    long_description=readme,
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    url='https://github.com/bwghughes/nosegrowl',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
