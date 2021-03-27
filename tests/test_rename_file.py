#!/usr/bin/env python3

''' requirements: 
        pythonfuzz (pip3 install pythonfuzz)
        the symlink xfce4_desktop_service in this directory linking to originating file
'''

from os import mkdir, system, getcwd
from xfce4_desktop_service import signal_handlers
from pythonfuzz.main import PythonFuzz

@PythonFuzz
def fuzz(buf):
    try:
        # create the test file
        try:
            system("touch ./test_files/test_file")
        except FileExistsError:
            pass

        current_directory = getcwd()

        test_name = buf.decode("utf-8")
        test_handler = signal_handlers()

        try:
            test_handler._rename(test_name, current_directory + "/test_files/test_file")
        except ValueError as e: # when we give the rename method an empty string
            print (e)             # this is what we want to happen
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