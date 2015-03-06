#!/usr/bin/env python

import os
import os.path
import sys
import distutils.core

ext = distutils.core.Extension('_transformations', sources = ['transformations.c'])

distutils.core.setup \
(name = 'transformations',
 version = '0.0.1',
 maintainer = 'Klee Dienes',
 maintainer_email = 'klee.dienes@hadronindustries.com',
 description = 'matrix library',
 py_modules = [ 'transformations' ],
 url = 'http://www.hadronindustries.com',
 ext_modules = [ ext ],
 )
