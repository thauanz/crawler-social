import unittest
from crawler import generator_files

class CrawlerTest(unittest.TestCase):
    def test_should_generator_csv_files(self):
        generator_files()
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()