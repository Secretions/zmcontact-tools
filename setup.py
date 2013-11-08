#!/usr/bin/env python

from distutils.core import setup
try:
    import py2exe
    from nsis import build_installer
except:
    build_installer = None

import zimbrasoap

setup(name='Zimbra Contact Tools',
      version=zimbrasoap.__version__,
      description='Suite of console utilities for interfacing with Zimbra contacts',
      author='Joaquin Lopez',
      author_email='mrgus@disco-zombie.net',
      scripts=['bin/zmcq'],
      cmdclass = {"py2exe": build_installer},
     )

