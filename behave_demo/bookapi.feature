Feature: Book API
    As an application developer
    I want an API that can add, retrieve and remove books

Scenario: Add a book
    Given endpoint "/books" is available
    When I HTTP POST "/books" with JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530637"
            },
            "title": "Wise Blood"
        }
        """
    Then the HTTP response status code is "201"
    When I HTTP GET "/books/0374530637"
    Then the HTTP response status code is "200"
    and the response body contains the JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530637"
            },
            "title": "Wise Blood"
        }
        """

Scenario: Attempt to re-add same book
    Given endpoint "/books" is available
    When I HTTP POST "/books" with JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530637"
            },
            "title": "Wise Blood"
        }
        """
    and I HTTP POST "/books" with JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530637"
            },
            "title": "Wise Blood"
        }
        """
    Then the HTTP response status code is "409"

Scenario: Attempt to retrieve a book that does not exist
    Given endpoint "/books" is available
    When I HTTP GET "/books/idontexist"
    Then the HTTP response status code is "404"

Scenario: Get books from empty library
    Given endpoint "/books" is available
    When I HTTP GET "/books"
    Then the HTTP response status code is "200"
    and "0" books are returned

Scenario: Get all books after adding two
    Given endpoint "/books" is available
    When I HTTP POST "/books" with JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530637"
            },
            "title": "Wise Blood"
        }
        """
    and I HTTP POST "/books" with JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530874"
            },
            "title": "The Violent Bear It Away"
        }
        """
    and I HTTP GET "/books"
    Then the HTTP response status code is "200"
    and "2" books are returned

Scenario: Attempt to delete a book that does not exist
    Given endpoint "/books" is available
    When I HTTP GET "/books/idontexist"
    Then the HTTP response status code is "404"

Scenario: Remove a book
    Given endpoint "/books" is available
    When I HTTP POST "/books" with JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530874"
            },
            "title": "The Violent Bear It Away"
        }
        """
    and I HTTP DELETE "/books/0374530874"
    Then the HTTP response status code is "200"
    When I HTTP GET "/books/0374530874"
    Then the HTTP response status code is "404"

Scenario: Remove all books when none exist
    Given endpoint "/books" is available
    When I HTTP DELETE "/books"
    Then the HTTP response status code is "200"

Scenario: Remove all books when some exist
    Given endpoint "/books" is available
    When I HTTP POST "/books" with JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530637"
            },
            "title": "Wise Blood"
        }
        """
    and I HTTP POST "/books" with JSON data:
        """
        {
            "identifier": {
                "ISBN-10": "0374530874"
            },
            "title": "The Violent Bear It Away"
        }
        """
    and I HTTP DELETE "/books"
    Then the HTTP response status code is "200"
    When I HTTP GET "/books"
    Then "0" books are returned
