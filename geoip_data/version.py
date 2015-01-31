# -*- coding: utf-8 -*-

import os

current = os.path.abspath(os.path.dirname(__file__))
version_filepath = os.path.abspath(os.path.join(current, 'version.txt'))

def get_version():
    with open(version_filepath) as fp:
        return fp.readline().strip()
    
def increment_version(major=False, minor=False, fixe=True):
    """
    TODO: gérer major/minor/fixe
    """
    
    current_version = get_version()

    with open(version_filepath, 'wb+') as fp:
        MAJOR, MINOR, FIXE = current_version.split('.')
        FIXE = int(FIXE) + 1
        new_value = "%s.%s.%s" % (MAJOR, MINOR, FIXE)
        fp.write(new_value)
        
#__VERSION__ = get_version()

if __name__ == "__main__":
    print(get_version())
