from distutils.core import setup
import py2exe
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")

setup(
    windows = ['pum.py'],
    options = {
        "py2exe": {
            "includes": ["sip", "PyQt4.QtCore", "PyQt4.QtGui", "requests", "json"]
            #, "dll_excludes": ["MSVCP90.dll"]
            #, "unbuffered": True
        }
    }
)
