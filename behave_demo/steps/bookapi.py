import requests


@given('endpoint "{path}" and method "{method}"')
def endpoint_and_method(context, path, method):
    context.path = path
    context.http_method = method

@given('the endpoint includes the id "{bookid}"')
@when('the endpoint includes the id "{bookid}"')
def add_id_to_endpoint(context, bookid):
    if context.path[-1] == "/":
        context.path += bookid
    else:
        context.path += ("/" + bookid)

@given('the payload includes the book')
@when('the payload includes the book')
def add_book_to_payload(context):
    if context.table:
        book = {'identifier': {}}
        book['identifier']['ISBN-10'] = context.table[0]['isbn10']
        book['title'] = context.table[0]['title']
        context.payload = book

@when('the endpoint is "{path}"')
def http_endpoint(context, path):
    context.path = path

@when('the method is "{method}"')
def http_method(context, method):
    context.http_method = method


@when('the request is executed')
def make_http_request(context):
    url = 'http://' + context.ip + ':' + context.port + context.path

    #temporary
    #canned_book = {'identifier': {'ISBN-10': "0374530637", 'ISBN-13': "978-0374530631", 'OCLC': "256887668"}, 'title': "Wise Blood", 'pages': 238, 'available': True, 'authors': ["Flannery O'Connor"]}

    if context.http_method.lower() == "get":
        context.r = requests.get(url, timeout=5)
    elif context.http_method.lower() == "post":
        context.r = requests.post(url, json=context.payload, timeout=5)
    elif context.http_method.lower() == "delete":
        context.r = requests.delete(url, timeout=5)


@then('the status code is "{code}"')
def assert_status_code(context, code):
    assert context.r.status_code == int(code)

@then('"{num_books}" books are returned')
def assert_status_code(context, num_books):
    assert len(context.r.json()['books']) == int(num_books)
