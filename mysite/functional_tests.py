from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    # Starts window
    def setUp(self):  
        self.browser = webdriver.Firefox()

    # Removes window
    def tearDown(self):  
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('CV_qualification')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def check_for_row_in_ex_table(self, row_text):
        table = self.browser.find_element_by_id('CV_experience')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # I log onto the cv section of my website
        self.browser.get('http://localhost:8000/cv')

        # The title says My CV
        self.assertIn('My CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('My CV', header_text)

        # I add an education item
        inputbox = self.browser.find_element_by_id("id_new_ed_item")  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'New education item'
        )

        # I add a new qualification
        inputbox.send_keys('BSc Computer Science - Test university * July 2020')  

        # The qualification is added
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  

        table = self.browser.find_element_by_id("CV_qualification")
        rows = table.find_elements_by_tag_name('tr')  
        
        # Add second item
        inputbox = self.browser.find_element_by_id("id_new_ed_item")
        inputbox.send_keys('A levels - Test college * July 2020')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Check qualifications
        self.check_for_row_in_list_table('BSc Computer Science - Test university')
        self.check_for_row_in_list_table('A levels - Test college * July 2017')

        # I add my work experience 
        table = self.browser.find_element_by_id("CV_experience")
        rows = table.find_elements_by_tag_name('tr')  
        
        inputbox = self.browser.find_element_by_id("id_new_ex_item")
        inputbox.send_keys('Job - Test Ltd * July 2016')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_ex_table('Job - Test Ltd')

# Checks if it's run from command line
if __name__ == '__main__':  
    unittest.main(warnings='ignore')  