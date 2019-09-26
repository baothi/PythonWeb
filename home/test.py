from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTestCase(SimpleTestCase):
    def text_home_page_status(seft):
        response = seft.client.get('/')
        seft.assertEquals(response.status_code, 201)
