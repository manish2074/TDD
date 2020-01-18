from selenium import webdriver
from lists.models import Item
from selenium.webdriver.common.keys import Keys
import time
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element__by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])    
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy a peacock feather')
        inputbox = self.browser.find_element_by_id('id_new_item')
        input.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy a peacock feather')
        self.check_for_row_in_list_table('2: Use a peacock feather')
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000/')
        # She notices the page title and header mention to-do lists
        print(self.browser.title)
        self.assertIn('lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('list', header_text)
       
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
        )
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])
        self.assertIn('2: Use a peacock feather', [row.text for row in rows])
        self.fail('Finish the test!')

class ItemModelTest(unittest.TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'THe first list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'THe second item in list'
        second_item.save()
        
        save_items = Item.objects.all()
        self.assertEqual(save_items.count(),2)

        first_saved_item = save_items[0]
        second_saved_item = save_items[1]
        self.assertEqual(first_saved_item.text,'HTe first list item')
        self.assertEqual(second_saved_item.text,'Item the second')
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')
