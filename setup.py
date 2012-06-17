#!/usr/bin/env python
#
# setup.py
#
# python-rrdtool distutil setup
#
# Primary author: Hye-Shik Chang <perky@fallin.lv>
# Maintainer: Piotr Banaszkiewicz <piotr@banaszkiewicz.org>
#
#  This file is part of python-rrdtool.
#
#  python-rrdtool is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  python-rrdtool is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.

from distutils.core import setup, Extension
from distutils.command.build import build
from distutils.spawn import find_executable
import os
import os.path


SOURCE = "rrdtool-1.4.7"
RRDBASE = os.environ.get('LOCALBASE', SOURCE + '/src')
library_dir = os.environ.get('BUILDLIBDIR', os.path.join(RRDBASE, '.libs'))
include_dir = os.environ.get('INCDIR', RRDBASE)


class configure(build):
    def run(self):
        executable = find_executable("configure", path=SOURCE)
        if executable:
            import subprocess
            executable = os.path.abspath(executable)
            subprocess.check_call(executable, cwd=os.path.dirname(executable))
        build.run(self)  # running parent, even though it seems empty


setup(
    name="python-rrdtool",
    version="1.4.7",
    description="Working Python RRDTool binding",
    author="Piotr Banaszkiewicz",
    author_email="piotr@banaszkiewicz.org",
    license="LGPL",
    url="http://oss.oetiker.ch/rrdtool",
    cmdclass={"build": configure},
    #packages=['rrdtool'],
    ext_modules=[
        Extension(
            "rrdtoolmodule",
            [SOURCE + "/bindings/python/rrdtoolmodule.c"],
            libraries=['rrd'],
            library_dirs=[library_dir],
            include_dirs=[include_dir],
        )
    ]
)
