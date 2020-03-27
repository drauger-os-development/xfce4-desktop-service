#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  autostart.py
#
#  Copyright 2020 Thomas Castleman <contact@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from __future__ import print_function
from sys import stderr
from os import getenv
from subprocess import Popen

# Make it easier for us to print to stderr
def eprint(*args, **kwargs):
	print(*args, file=stderr, **kwargs)

DE = (getenv("XDG_CURRENT_DESKTOP")).upper()
if (DE == "XFCE"):
	Popen("/usr/bin/xfce4-desktop-service")
else:
	eprint("Xfce not running. Exiting . . .")


