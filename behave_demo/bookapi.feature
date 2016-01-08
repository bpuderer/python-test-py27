Feature: Book API
    As an application developer
    I want an API that can add, retrieve, and remove books
    So that I can create a library app

Scenario: Add a book
    Given I use ip "localhost" and port "default"
    When I HTTP POST the path "/books"
    Then the status code is "201"

Scenario: Add a duplicate book
    Given I use ip "localhost" and port "default"
    When I HTTP POST the path "/books"
    Then the status code is "201"
    When I HTTP POST the path "/books"
    Then the status code is "409"

Scenario: Get all books
    Given I use ip "localhost" and port "default"
    When I HTTP GET the path "/books"
    Then the status code is "200"

Scenario: Remove all books
    Given I use ip "localhost" and port "default"
    When I HTTP DELETE the path "/books"
    Then the status code is "200"
