"""
In this approach:

We import the my_module module containing the add function.
We use the @patch decorator directly on the import statement to patch the add function with a MagicMock object.
We configure the MagicMock object to return the desired mock return value (5) when called.
Inside the test case method, we call my_module.add, which is now replaced by the MagicMock object.
Since the MagicMock object is configured to return 5, the result of calling my_module.add(2, 3) will be 5.
We then assert that the result matches the expected mock return value (5).
This ensures that the original add function is completely replaced by the MagicMock object, and its implementation is not executed at all during the test.

"""
import unittest
from unittest.mock import patch, MagicMock
import my_module  # Import the module containing the add function

class TestAddFunction(unittest.TestCase):
    @patch('my_module.add', MagicMock(return_value=5))
    def test_add_function(self):
        # Call the add function (the patched version, not the actual add function)
        result = my_module.add(2, 3)

        # Assert that the result matches the expected mock return value
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
