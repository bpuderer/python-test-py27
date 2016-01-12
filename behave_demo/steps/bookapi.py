import requests
import json


@given('endpoint "{path}" is available')
def endpoint_available(context, path):
    r = requests.head(context.base_url + path, timeout=5)
    assert r.status_code == 200

@when('I HTTP POST "{path}" with JSON data')
def http_post(context, path):
    url = context.base_url + path
    context.r = requests.post(url, json=json.loads(context.text), timeout=5)

@when('I HTTP GET "{path}"')
def http_get(context, path):
    url = context.base_url + path
    context.r = requests.get(url, timeout=5)

@when('I HTTP DELETE "{path}"')
def http_delete(context, path):
    url = context.base_url + path
    context.r = requests.delete(url, timeout=5)

@then('the HTTP response status code is "{code}"')
def assert_status_code(context, code):
    assert context.r.status_code == int(code)

@then('"{num_books}" books are returned')
def assert_status_code(context, num_books):
    assert len(context.r.json()['books']) == int(num_books)

@then('the response body contains the JSON data')
def assert_response_json(context):
    actual_response = context.r.json()
    expected_response = json.loads(context.text)
    assert actual_response == expected_response
