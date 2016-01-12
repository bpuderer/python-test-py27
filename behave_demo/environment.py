import requests


def before_scenario(context, scenario):
    """equivalent of unittest setUp"""
    ip = "localhost"
    port = "1234"
    context.base_url = "http://" + ip + ":" + port
    requests.delete(context.base_url + '/books', timeout=5)

def after_scenario(context, scenario):
    """equivalent of unittest tearDown"""
    requests.delete(context.base_url + '/books', timeout=5)
