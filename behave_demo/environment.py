import requests

def before_scenario(context, scenario):
    """equivalent of unittest setUp"""
    requests.delete('http://localhost:1234/books', timeout=5)

def after_scenario(context, scenario):
    """equivalent of unittest tearDown"""
    requests.delete('http://localhost:1234/books', timeout=5)
