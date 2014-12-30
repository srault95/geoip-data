# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from geoip_data import __VERSION__


setup(
    name='geoip-data',
    version=__VERSION__,
    description='Data finder for Pygeoip',
    author='Stéphane RAULT',
    author_email='stephane.rault@radicalspam.org',
    url='https://github.com/srault95/geoip-data',
    include_package_data=True,
    packages=find_packages(),
)
