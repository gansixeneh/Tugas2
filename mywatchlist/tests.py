# from django.test import TestCase

import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Membuat Client
        self.client = Client()

    def test_details(self):
        # Melakukan request GET
        response = self.client.get('/mywatchlist/html/')

        # Menguji apakah URL yang ada dapat mengembalikan respon HTTP 200 OK
        self.assertEqual(response.status_code, 200)

        # Melakukan request GET
        response = self.client.get('/mywatchlist/xml/')

        # Menguji apakah URL yang ada dapat mengembalikan respon HTTP 200 OK
        self.assertEqual(response.status_code, 200)

        # Melakukan request GET
        response = self.client.get('/mywatchlist/json/')

        # Menguji apakah URL yang ada dapat mengembalikan respon HTTP 200 OK
        self.assertEqual(response.status_code, 200)