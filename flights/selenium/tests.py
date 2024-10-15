import os
import pathlib
import unittest
import time  # Import time for adding a delay
from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

class WebpageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get(file_uri("counter.html"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_title(self):
        self.assertEqual(self.driver.title, "Counter")

    def test_increase(self):
        increase = self.driver.find_element(By.ID, "increase")
        increase.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "1")

    def test_decrease(self):
        decrease = self.driver.find_element(By.ID, "decrease")
        decrease.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increase(self):
        increase = self.driver.find_element(By.ID, "increase")
        for _ in range(3):
            increase.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "3")

if __name__ == "__main__":
    unittest.main()
    time.sleep(5)  # Wait for 5 seconds before closing the browser
