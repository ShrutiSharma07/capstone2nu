from selenium import webdriver
import pytest
import unittest2
import time

# driver.get("http://www.google.com")

class TestSelenium(unittest2.TestCase):

    def setUp (self):
        print(" Capstone sample test case ")
        self.driver = webdriver.Chrome(r"Browsers/chromedriver")

        self.driver.maximize_window()
        self.driver.get("file:///Users/shrush/capstone2nu/tests/src/unittest/python/web/index.html")

    def test_selenium (self):

        self.driver.find_element_by_id("Field1").send_keys("Shruti")
        time.sleep(2)
        self.driver.find_element_by_id("Field2").send_keys("Sharma")
        time.sleep(2)
        self.driver.find_element_by_id("Field3").send_keys("abc@xyz.com")
        time.sleep(2)
        self.driver.find_element_by_id("Field4").send_keys("Hey bot! How has your automation been?")
        time.sleep(2)
        self.driver.find_element_by_id("Field5_2").click()
        time.sleep(2)
        self.driver.find_element_by_id("Field6").click()
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="Field106"]/option[3]').click()

        self.driver.find_element_by_id("saveForm").click()
        time.sleep(3)

        self.driver.switch_to.alert.accept()

    def tearDown (self):

        print("Tests successfully ended")
        self.driver.close()


if __name__ == '_main_':
    unittest2.main()