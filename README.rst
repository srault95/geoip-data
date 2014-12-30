GeoIP datas for Pygeoip
=======================

::

    >>> import os
    >>> from geoip_data import where_country_ipv4
    >>> where_country_ipv4()
    '/usr/local/lib/python2.7/dist-packages/geoip_data/GeoIP.dat'
    
    >>> from geoip_data import where_country_ipv4
    >>> import pygeoip
    >>> filepath = where_country_ipv4()
    >>> country_v4 = pygeoip.GeoIP(filepath, flags=pygeoip.MMAP_CACHE)
    >>> country_v4.country_code_by_addr('64.233.161.99')
    'US'
    
    