from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from CV.views import cv_page  

class PageTest(TestCase):

    #def test_url_resolves_to_page_view(self):
     #   found = resolve('/cv')  
      #  self.assertEqual(found.func, cv_page) 
    

    def test_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.strip().startswith('<html>'))  
        self.assertIn('<title>My CV</title>', html)  
        self.assertTrue(html.strip().endswith('</html>'))

    def test_uses_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv_base.html')