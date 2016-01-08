import requests


@given('I use ip "{ip}" and port "{port}"')
def set_ip_port(context, ip, port):
    context.ip = ip
    if port == "default":
        context.port = "1234"
    else:
        context.port = port

@when('I HTTP GET the path "{path}"')
def http_get_request(context, path):
    url = "http://" + context.ip + ":" + context.port + path
    context.r = requests.get(url, timeout=5)

@when('I HTTP POST the path "{path}"')
def http_post_request(context, path):
    canned_book = {'identifier': {'ISBN-10': "0374530637", 'ISBN-13': "978-0374530631", 'OCLC': "256887668"}, 'title': "Wise Blood", 'pages': 238, 'available': True, 'authors': ["Flannery O'Connor"]}
    url = "http://" + context.ip + ":" + context.port + path
    context.r = requests.post(url, json=canned_book, timeout=5)

@when('I HTTP DELETE the path "{path}"')
def http_delete_request(context, path):
    url = "http://" + context.ip + ":" + context.port + path
    context.r = requests.delete(url, timeout=5)

@then('the status code is "{code}"')
def assert_status_code(context, code):
    assert context.r.status_code == int(code)
