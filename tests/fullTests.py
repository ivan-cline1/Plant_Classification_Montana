import unittest
import tempfile
import os
import numpy as np
import sys
sys.path.append('.\\scripts')

from imageClean import CleanCSV, CountInstancesAndWriteToTXT, CreateCSVWithOnlyTopClasses, cleanImages

class TestImageProcessingFunctions(unittest.TestCase):
    
    def setUp(self):
        self.sample_data_location = ".\\tests\\testData\\raw\\testRaw.csv"
        self.sample_clean_data_path = ".\\tests\\testData\\interim"
    def test_CleanImages(self):

        cleaned_data = cleanImages(self.sample_data_location,5,self.sample_clean_data_path)

        # expected_cleaned_data = ["CATEGORY_1", "CATEGORY_2", "CATEGORY_1", "CATEGORY_3", "CATEGORY_2"]
        
        # self.assertEqual(cleaned_data, expected_cleaned_data)
    def test_readImages(self):
        pass

if __name__ == '__main__':
    unittest.main()
