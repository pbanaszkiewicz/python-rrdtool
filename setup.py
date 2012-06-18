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

from distutils.core import setup, Extension, Command
from distutils.command.build import build
from distutils.command.build_ext import build_ext
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


class BuildConfigure(Command):
    description = "Generate configuration files using ./configure (autoconf)"

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if not os.path.exists(os.path.join(SOURCE, "config.status")):
            executable = find_executable("configure", path=SOURCE)
            if executable:
                import subprocess
                executable = os.path.abspath(executable)
                os.chmod(executable, 0777)
                subprocess.check_call(executable, cwd=os.path.dirname(executable))


class BuildExtension(build_ext):
    def run(self):
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        build_ext.run(self)

    sub_commands = [("build_configure", None)] + build_ext.sub_commands


setup(
    name="python-rrdtool",
    version="1.4.7",
    description="Working Python RRDTool binding",
    author="Piotr Banaszkiewicz",
    author_email="piotr@banaszkiewicz.org",
    license="LGPL",
    url="http://oss.oetiker.ch/rrdtool",
    cmdclass={"build_configure": BuildConfigure, "build_ext": BuildExtension},
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
