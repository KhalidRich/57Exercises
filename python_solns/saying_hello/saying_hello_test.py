# This is the test suite for Exercise 1 of "Exercises for Programmers".
# Oct 12, 2016

import unittest
from saying_hello import hello_str

class SayingHelloTest(unittest.TestCase):
    def test_blank_name(self):
        # Should test blank name
        hello_msg = hello_str()
        self.assertEqual(hello_msg, "Hello there, stranger!")
    
    def test_standard_name(self):
        # Should test standard name
        hello_msg = hello_str("John Doe")
        self.assertEqual(hello_msg, "Hello there, John Doe!")

    def test_hello_world(self):
        hello_msg_lower = hello_str("world")
        hello_msg_upper = hello_str("world")
        self.assertEqual(hello_msg_lower, "Hello world!")
        self.assertEqual(hello_msg_lower, hello_msg_upper)


if __name__ == "__main__":
    unittest.main()
