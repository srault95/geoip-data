# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from geoip_data import __VERSION__

with open("README.rst") as fp:
    long_description = fp.read()

setup(
    name='geoip-data',
    version=__VERSION__,
    description='Simple dat file finder for pygeoip',
    long_description=long_description,
    author='Stéphane RAULT',
    author_email='stephane.rault@radicalspam.org',
    url='https://github.com/srault95/geoip-data',
    include_package_data=True,
    packages=find_packages(),
)
