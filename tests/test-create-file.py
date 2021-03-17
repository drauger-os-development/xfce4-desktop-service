import sys
sys.path.append("../usr/bin")

from unittest import TestCase, main
from xfce4-desktop-service import signal_handlers

class CreateFileTest(TestCase):
    def test_custom_create_file(self):
        test_handler = signal_handlers()

        test_handler._custom_create_file("~/Desktop", "a test", False)

main()