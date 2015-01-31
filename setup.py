# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from geoip_data.version import get_version

with open("README.rst") as fp:
    long_description = fp.read()

setup(
    name='geoip-data',
    version=get_version(),
    description='Simple dat file finder for pygeoip',
    long_description=long_description,
    author='Stéphane RAULT',
    author_email='stephane.rault@radicalspam.org',
    url='https://github.com/srault95/geoip-data',
    include_package_data=True,
    packages=find_packages(),
)
