import requests


@given('endpoint "{path}" and method "{method}"')
def endpoint_and_method(context, path, method):
    context.path = path
    context.http_method = method

@when('the request is executed')
def make_http_request(context):
    url = 'http://' + context.ip + ':' + context.port + context.path

    #temporary
    canned_book = {'identifier': {'ISBN-10': "0374530637", 'ISBN-13': "978-0374530631", 'OCLC': "256887668"}, 'title': "Wise Blood", 'pages': 238, 'available': True, 'authors': ["Flannery O'Connor"]}

    if context.http_method.lower() == "get":
        context.r = requests.get(url, timeout=5)
    elif context.http_method.lower() == "post":
        context.r = requests.post(url, json=canned_book, timeout=5)
    elif context.http_method.lower() == "delete":
        context.r = requests.delete(url, timeout=5)


@then('the status code is "{code}"')
def assert_status_code(context, code):
    assert context.r.status_code == int(code)
