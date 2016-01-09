import requests

def before_scenario(context, scenario):
    """equivalent of unittest setUp"""
    context.ip = "localhost"
    context.port = "1234"
    requests.delete('http://' + context.ip + ':' + context.port + '/books', timeout=5)

def after_scenario(context, scenario):
    """equivalent of unittest tearDown"""
    requests.delete('http://' + context.ip + ':' + context.port + '/books', timeout=5)
