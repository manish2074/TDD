from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):

    ''' 
    This is refactoring. Long code into short but the functionality of the ocde is same.
    '''
    # def test_root_url_resolves_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf8')
    #     excepted_html = render_to_string('home.html')
    #     self.assertEqual(html,expected_html)
    
    def test_users_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    '''
    Ya samma
    '''

    def test_can_save_a_POST_request(self):
        self.client.post('/',data={'item_text':'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')
        
        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response,'home.html')
    def test_redirect_after_POST(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertEqual(response.status_code,302)
        self.assertEqual(respne['location'],'/')


    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(),0)

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemno 1')
        Item.objects.create(text='itemno 2')
        response = self.client.get('/')
        self.assertIn('itemno 1',response.content.decode())
        self.assertIn('itemno 2',response.content.decode())
