#!/usr/bin/python
#
# python-lxc: Python bindings for LXC
#
# (C) Copyright Canonical Ltd. 2012
#
# Authors:
# Stephane Graber <stgraber@ubuntu.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from distutils.core import setup, Extension

module = Extension('_lxc', sources=['lxc.c'], libraries=['lxc'])

setup(name='lxc-python2',
      version='0.1',
      description='Python2 bindings for LXC',
      long_description='The lxc-python2 package contains lxc bindings for python2',
      license='LGPLv2+',
      maintainer='lxc',
      maintainer_email='lxc-devel@lists.linuxcontainers.org',
      url='git://github.com/lxc/python2-lxc',
      packages=['lxc'],
      package_dir={'lxc': 'lxc'},
      ext_modules=[module])
