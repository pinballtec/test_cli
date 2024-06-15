import unittest
import shutil
import os
import sys
from fixed_width_file.fixed_width_file import FixedWidthFile


class TestFixedWidthFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if len(sys.argv) != 2:
            print("Usage: python -m unittest tests/test_fixed_width_file.py <path_to_sample_file>")
            sys.exit(1)
        cls.original_filepath = sys.argv[1]
        cls.test_filepath = "test_sample_fixed_width_file.txt"
        # Remove the filepath argument so unittest doesn't try to interpret it
        sys.argv.pop()

    def setUp(self):
        shutil.copyfile(self.original_filepath, self.test_filepath)
        self.file = FixedWidthFile(self.test_filepath)

    def tearDown(self):
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)

    def test_get_field(self):
        self.file = FixedWidthFile(self.test_filepath)
        self.assertEqual(self.file.get_field("header", "name"), "John")

    def test_set_field(self):
        self.file.set_field("header", "name", "Jane")
        self.file.save_file()
        self.file = FixedWidthFile(self.test_filepath)
        self.assertEqual(self.file.get_field("header", "name"), "Jane")

    def test_add_transaction(self):
        initial_count = len(self.file.transactions)
        self.file.add_transaction("1000", "USD")
        self.file.save_file()
        self.file = FixedWidthFile(self.test_filepath)
        self.assertEqual(len(self.file.transactions), initial_count + 1)


if __name__ == "__main__":
    unittest.main()
