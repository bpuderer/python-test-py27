import unittest
import requests
#import json


class UnitTestExample(unittest.TestCase):

    def setUp(self):
        """setting up test"""
        pass

    def tearDown(self):
        """tearing down test
        only runs if setUp successful"""
        pass

    def test_book_retrieval(self):
        """test retrieving the canned book in the sim"""
        r = requests.get("http://localhost:1234/", timeout=5)

        book = r.json()
        #book = json.loads(r.text)

        self.assertEqual(r.status_code, 200)
        #new in python 2.7, auto calling of type specific equality function
        self.assertEqual(book['identifier']['ISBN-10'], "0374530637")
        self.assertEqual(book['identifier']['ISBN-13'], "978-0374530631")
        self.assertEqual(book['identifier']['OCLC'], "256887668")
        self.assertEqual(book['title'], "Wise Blood")
        self.assertEqual(book['pages'], 238)
        self.assertTrue(book['available'])
        self.assertEqual(book['authors'], ["Flannery O'Connor"])

    def test_book_creation(self):
        """test posting json to the sim and confirming response code"""
        book = {'identifier': {'ISBN-10': "0374530874", 'ISBN-13': "978-0374530877", 'OCLC': "170140"}, 'title': "The Violent Bear It Away", 'pages': 243, 'available': True, 'authors': ["Flannery O'Connor"]}

        r = requests.post("http://localhost:1234/", json=book, timeout=5)
        self.assertEqual(r.status_code, 201)
        #once sim can store books more assertions and cases will be added

if __name__ == '__main__':
    unittest.main(verbosity=2)
