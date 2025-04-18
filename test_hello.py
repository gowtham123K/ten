import unittest
from test_hello import greet  

class TestGreet(unittest.TestCase):
    def test_greet_output(self):
        self.assertEqual(greet(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()