import datetime
from django.test import TestCase
from .models import Report


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class mineTest(TestCase):
    def setup(self):
        Report.objects.create(worker = 'Thiliban', date = datetime.datetime(2011, 04, 10),process = 'Ideeli',  count = 158, error = 41)
        #Report.objects.create(worker = 'Venkat', date = '01/09/2015',process = 'Ideeli',  count = 158, error = 41)
    def test_see(self):
        self.assertTrue(Report.objects.filter(worker = 'Thiliban'), None)
        #Report.objects.get(worker = 'Venkat')
class PollsViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/sop/')
        self.assertEqual(resp.status_code, 200)
