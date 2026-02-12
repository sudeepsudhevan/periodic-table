import unittest
import os
from bs4 import BeautifulSoup

class TestPeriodicTable(unittest.TestCase):
    def setUp(self):
        # Path to the index.html file
        self.file_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')
        
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
        
        self.soup = BeautifulSoup(self.content, 'html.parser')

    def test_title(self):
        """Test that the title is correct"""
        self.assertEqual(self.soup.title.string, "Periodic Table")

    def test_hydrogen_exists(self):
        """Test that Hydrogen element exists"""
        # Search for text "Hydrogen" in any span
        element = self.soup.find('span', string="Hydrogen")
        self.assertIsNotNone(element, "Hydrogen element not found")

    def test_structure(self):
        """Test basic structure exists"""
        self.assertIsNotNone(self.soup.find('div', class_='container'), "Main container not found")
        self.assertIsNotNone(self.soup.find('div', class_='left-div'), "Left division not found")

if __name__ == '__main__':
    unittest.main()
