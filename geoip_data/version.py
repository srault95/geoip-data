# -*- coding: utf-8 -*-

import os

current = os.path.abspath(os.path.dirname(__file__))
version_filepath = os.path.abspath(os.path.join(current, 'version.txt'))

def get_version():
    with open(version_filepath) as fp:
        return fp.readline().strip()
    
if __name__ == "__main__":
    print(get_version())
