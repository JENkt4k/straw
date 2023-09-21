import subprocess
import bpy
import sys

py_exec =  sys.exec_prefix + "\\bin\\python.exe"
# ensure pip is installed & update
subprocess.call([str(py_exec), "-m", "ensurepip"])
subprocess.call([str(py_exec), "-m", "pip", "install", "--upgrade", "pip"])
# install dependencies using pip
# dependencies such as 'numpy' could be added to the end of this command's list
subprocess.call([str(py_exec),"-m", "pip", "install", "scipy numpy"])