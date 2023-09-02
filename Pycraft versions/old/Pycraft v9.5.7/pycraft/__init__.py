print("Thank you for using Pycraft!\nPlease wait, we are getting it ready for you now.")

import sys
import pathlib
import platform
import os

# caution: path[0] is reserved for script path (or '' in REPL)
base_folder = pathlib.Path(os.path.dirname(__file__))
sys.pycache_prefix = base_folder / "temporary"

import ctypes

programs_base_folder = base_folder / "programs"
installer_base_folder = base_folder / "programs" / "installer"
utility_base_folder = base_folder / "programs" / "utility"

sys.path.append(str(programs_base_folder))
sys.path.append(str(installer_base_folder))
sys.path.append(str(utility_base_folder))

from pycraft_main import QueryVersion
from pycraft_main import start

if platform.system() == "Windows":
    myappid = f'PycraftDev.Pycraft._.{QueryVersion()}' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    del myappid

del sys
del os
del pathlib
del platform
del ctypes
del base_folder
del installer_base_folder
del utility_base_folder
del programs_base_folder