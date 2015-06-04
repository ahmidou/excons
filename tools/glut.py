# Copyright (C) 2009, 2010  Gaetan Guidet
#
# This file is part of excons.
#
# excons is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or (at
# your option) any later version.
#
# excons is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA.

from SCons.Script import *
import sys
import excons

def Require(env):
  glutinc, glutlib = excons.GetDirs("glut")
  
  glutlibsuffix = excons.GetArgument("glut-libsuffix", "")
  
  if glutinc:
    env.Append(CPPPATH=[glutinc])
  
  if glutlib:
    env.Append(LIBPATH=[glutlib])
  
  if sys.platform == "win32":
    env.Append(CPPDEFINES=["GLUT_NO_LIB_PRAGMA"])
    if excons.Build64():
      env.Append(LIBS=["glut64%s" % glutlibsuffix])
      
    else:
      env.Append(LIBS=["glut32"])
  
  elif sys.platform == "darwin":
    env.Append(LINKFLAGS=" -framework GLUT")
  
  else:
    env.Append(LIBS=["glut%s" % glutlibsuffix])
