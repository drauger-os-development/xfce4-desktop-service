#!/usr/bin/env python3

''' requirements: 
        pythonfuzz (pip3 install pythonfuzz)
        the symlink xfce4_desktop_service in this directory linking to originating file
'''

from os import mkdir, system
from xfce4_desktop_service import signal_handlers
from pythonfuzz.main import PythonFuzz

@PythonFuzz
def fuzz(buf):
    try:
        test_name = buf.decode("utf-8")
        test_handler = signal_handlers()
        test_handler._custom_create_file("./test_files", test_name, False)
    except (UnicodeDecodeError):
        pass

    
if __name__ == '__main__':
    # set up
    try:
        mkdir("./test_files")
    except FileExistsError:
        pass

    fuzz() # touch fuzzy, get dizzy

    # clean up
    system("rm -r ./test_files")