from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from CV.views import cv_page  

class PageTest(TestCase):

    #def test_url_resolves_to_page_view(self):
     #   found = resolve('/cv')  
      #  self.assertEqual(found.func, cv_page) 
    
    def test_uses_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv_base.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/cv', data={'ed_item_text': 'New education item'})
        self.assertIn('New education item', response.content.decode())
        self.assertTemplateUsed(response, 'cv_base.html')
        self.assertIn('BSc Computer Science - Test university', [row.text for row in rows])