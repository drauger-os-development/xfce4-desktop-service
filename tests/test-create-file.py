#!/usr/bin/env python3
# import sys
import os
# sys.path.append("../usr/bin")

from unittest import TestCase, main
from xfce4_desktop_service import signal_handlers

class CreateFileTest(TestCase):
    def test_custom_create_file(self):
        test_handler = signal_handlers()

        print("CREATE FILE TEST: ", end="")
        test_handler._custom_create_file(".", "test", False)
        if os.path.isfile("test"):
        	print("PASS")
        	os.remove("test")
        else:
        	print("FAIL")
main()
