Feature: Book API
    As an application developer
    I want an API that can add, retrieve, and remove books
    So that I can create a library app

Scenario: Add a book
    Given endpoint "/books" and method "post"
    When the request is executed
    Then the status code is "201"

Scenario: Re-add same book
    Given endpoint "/books" and method "post"
    When the request is executed
    Then the status code is "201"
    When the request is executed
    Then the status code is "409"
    
Scenario: Get all books
    Given endpoint "/books" and method "get"
    When the request is executed
    Then the status code is "200"

Scenario: Remove all books
    Given endpoint "/books" and method "delete"
    When the request is executed
    Then the status code is "200"
