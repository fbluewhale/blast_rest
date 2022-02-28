from django.test import TestCase
from django_webtest import WebTest

from blastplus import settings


class BlastTestCase(TestCase):
    def test_blastn(self):
        resp = self.client.get('/blastn/')
        self.assertEqual(resp.status_code, 200)
        
    def test_tblastn(self):
        resp = self.client.get('/tblastn/')
        self.assertEqual(resp.status_code, 200)

    def test_blastp(self):
        resp = self.client.get('/blastp/')
        self.assertEqual(resp.status_code, 200)

    def test_blastx(self):
        resp = self.client.get('/blastx/')
        self.assertEqual(resp.status_code, 200)

