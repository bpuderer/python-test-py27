import httplib
import unittest
import requests


class UnitTestExample(unittest.TestCase):

    def setUp(self):
        """setting up test"""
        requests.delete("http://localhost:1234/books", timeout=5)

    def tearDown(self):
        """tearing down test
        only runs if setUp successful"""
        requests.delete("http://localhost:1234/books", timeout=5)

    def test_book_creation(self):
        """verify book creation"""
        book = {'identifier': {'ISBN-10': "0374530874"}, 'title': "The Violent Bear It Away"}
        r = requests.post("http://localhost:1234/books", json=book, timeout=5)
        self.assertEqual(r.status_code, httplib.CREATED)

    def test_duplicate_book(self):
        """attempt duplicate book creation"""
        url = "http://localhost:1234/books"
        book = {'identifier': {'ISBN-10': "0374530874"}, 'title': "The Violent Bear It Away"}
        requests.post(url, json=book, timeout=5)
        r = requests.post(url, json=book, timeout=5)
        self.assertEqual(r.status_code, httplib.CONFLICT)

    def test_book_same_title(self):
        """verify creating multiple books with same title"""
        url = "http://localhost:1234/books"
        book = {'identifier': {'ISBN-10': "0374530874"}, 'title': "The Violent Bear It Away"}
        requests.post(url, json=book, timeout=5)
        book['identifier']['ISBN-10'] = "0374530875"
        r = requests.post(url, json=book, timeout=5)
        self.assertEqual(r.status_code, httplib.CREATED)

    def test_book_retrieval(self):
        """verify retrieving a book"""
        url = "http://localhost:1234/books"
        book = {'identifier': {'ISBN-10': "0374530874"}, 'title': "The Violent Bear It Away"}
        requests.post(url, json=book, timeout=5)
        r = requests.get(url + '/' + book['identifier']['ISBN-10'], timeout=5)
        res_body = r.json()
        self.assertEqual(r.status_code, httplib.OK)
        self.assertEqual(res_body['identifier']['ISBN-10'], book['identifier']['ISBN-10'])
        self.assertEqual(res_body['title'], book['title'])

    def test_nonexistent_book_retrieval(self):
        """attempt to retrieve book that does not exist"""
        r = requests.get("http://localhost:1234/books/idontexist", timeout=5)
        self.assertEqual(r.status_code, httplib.NOT_FOUND)

    def test_get_all_books_empty(self):
        """retrieve all books when none exist"""
        r = requests.get("http://localhost:1234/books", timeout=5)
        self.assertEqual(r.status_code, httplib.OK)
        self.assertFalse(r.json()['books'])

    def test_retrieve_books(self):
        """retrieve all books when some exist"""
        url = "http://localhost:1234/books"
        book = {'identifier': {'ISBN-10': "0374530874"}, 'title': "The Violent Bear It Away"}
        requests.post(url, json=book, timeout=5)
        book = {'identifier': {'ISBN-10': "0374530637"}, 'title': "Wise Blood"}
        requests.post(url, json=book, timeout=5)        
        r = requests.get(url, timeout=5)
        self.assertEqual(r.status_code, httplib.OK)
        self.assertEqual(len(r.json()['books']), 2)

    def test_nonexistent_book_removal(self):
        """attempt to remove a book that does not exist"""
        r = requests.delete("http://localhost:1234/books/idontexist", timeout=5)
        self.assertEqual(r.status_code, httplib.NOT_FOUND)

    def test_book_removal(self):
        """verify removing a book"""
        url = "http://localhost:1234/books"
        book = {'identifier': {'ISBN-10': "0374530874"}, 'title': "The Violent Bear It Away"}
        requests.post(url, json=book, timeout=5)
        r = requests.delete(url + '/' + book['identifier']['ISBN-10'], timeout=5)
        self.assertEqual(r.status_code, httplib.OK)
        r = requests.get(url + '/' + book['identifier']['ISBN-10'], timeout=5)
        self.assertEqual(r.status_code, httplib.NOT_FOUND)

    def test_remove_all_books_empty(self):
        """remove all on empty library"""
        r = requests.delete("http://localhost:1234/books", timeout=5)
        self.assertEqual(r.status_code, httplib.OK)
        
    def test_remove_all_books_some_exist(self):
        """remove all books when some exist"""
        url = "http://localhost:1234/books"
        book = {'identifier': {'ISBN-10': "0374530874"}, 'title': "The Violent Bear It Away"}
        requests.post(url, json=book, timeout=5)
        book = {'identifier': {'ISBN-10': "0374530637"}, 'title': "Wise Blood"}
        requests.post(url, json=book, timeout=5)        
        r = requests.delete(url, timeout=5)
        self.assertEqual(r.status_code, httplib.OK)
        r = requests.get(url, timeout=5)
        self.assertFalse(r.json()['books'])

    def test_book_creation_invalid_json(self):
        """attempt to create a book with invalid json"""
        invalid_json = [{'identifier': {'ISBN-13': "978-0374530631"}, 'title': "Wise Blood"},
                        {'identifier': {'ISBN-10': None}, 'title': "Wise Blood"},
                        {'identifier': {'ISBN-10': "         "}, 'title': "Wise Blood"},
                        {'identifier': {'ISBN-10': 3745306370}, 'title': "Wise Blood"},
                        {'title': "Wise Blood"},
                        {'identifier': {'ISBN-10': "0374530637"}},
                        {'identifier': {'ISBN-10': "0374530637"}, 'title': None},
                        {'identifier': {'ISBN-10': "0374530637"}, 'title': ""},
                        {'identifier': {'ISBN-10': "0374530637"}, 'title': []}]
        for payload in invalid_json:
            r = requests.post("http://localhost:1234/books", json=payload, timeout=5)
            self.assertEqual(r.status_code, httplib.BAD_REQUEST)


if __name__ == '__main__':
    unittest.main(verbosity=2)
