from django.test import SimpleTestCase

from django.urls import reverse


from django.test import SimpleTestCase 
from django.urls import reverse, resolve
from .views import HomePageView



class HomepageTests(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self): 

        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_homepage_contains_home_page(self): 

        self.assertContains(self.response, 'Homepage')
    
    def test_homepage_doesnt_contain(self): 

        self.assertNotContains(self.response, 'Whatever you  say here')
    
    def test_homepage_url_resolves_homepageview(self): 
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__)