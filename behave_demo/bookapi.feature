Feature: Book API
    As an application developer
    I want an API that can add, retrieve, and remove books
    So that I can create a library app

Scenario: Add a book
    Given endpoint "/books" and method "post"
    and the payload includes the book
        |isbn10    |title     |
        |0374530637|Wise Blood|
    When the request is executed
    Then the status code is "201"

Scenario: Attempt to re-add same book
    Given endpoint "/books" and method "post"
    and the payload includes the book
        |isbn10    |title     |
        |0374530637|Wise Blood|
    When the request is executed
    Then the status code is "201"
    When the request is executed
    Then the status code is "409"

Scenario: Attempt to retrieve a book that does not exist
    Given endpoint "/books" and method "get"
    and the endpoint includes the id "idontexist"
    When the request is executed
    Then the status code is "404"

Scenario: Get books from empty library
    Given endpoint "/books" and method "get"
    When the request is executed
    Then the status code is "200"
    and "0" books are returned

Scenario: Get all books after adding two
    Given endpoint "/books" and method "post"
    and the payload includes the book
        |isbn10    |title                   |
        |0374530874|The Violent Bear It Away|
    When the request is executed
    Then the status code is "201"
    When the payload includes the book
        |isbn10    |title     |
        |0374530637|Wise Blood|
    and the request is executed
    Then the status code is "201"
    When the method is "get"
    and the request is executed
    Then the status code is "200"
    and "2" books are returned

Scenario: Attempt to delete a book that does not exist
    Given endpoint "/books" and method "delete"
    and the endpoint includes the id "idontexist"
    When the request is executed
    Then the status code is "404"

Scenario: Remove a book
    Given endpoint "/books" and method "post"
    and the payload includes the book
        |isbn10    |title                   |
        |0374530874|The Violent Bear It Away|
    When the request is executed
    Then the status code is "201"
    When the method is "delete"
    and the endpoint includes the id "0374530874"
    and the request is executed
    Then the status code is "200"
    When the method is "get"
    and the request is executed
    Then the status code is "404"

Scenario: Remove all books when some exist
    Given endpoint "/books" and method "post"
    and the payload includes the book
        |isbn10    |title                   |
        |0374530874|The Violent Bear It Away|
    When the request is executed
    Then the status code is "201"
    When the payload includes the book
        |isbn10    |title     |
        |0374530637|Wise Blood|
    and the request is executed
    Then the status code is "201"
    When the method is "delete"
    and the request is executed
    Then the status code is "200"
    When the method is "get"
    and the request is executed
    Then the status code is "200"
    and "0" books are returned

Scenario: Remove all books when none exist
    Given endpoint "/books" and method "delete"
    When the request is executed
    Then the status code is "200"
