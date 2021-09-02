import unittest
from hello import Hello


class TestHello(unittest.TestCase):
    def test_say(self):
        hello = Hello()
        self.assertEqual(hello.say(), "Hello World")
