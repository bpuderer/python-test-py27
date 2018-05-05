from httplib import NOT_FOUND
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    def on_start(self):
        print("on_start!")

    @task(10) # optional weight. @task, @task(weight)
    def all_books(self):
        # client is an instance of HttpSession created when Locust instantiated
        # HttpSession is a subclass of requests.Session
        # http://docs.python-requests.org/en/master/api/#request-sessions
        self.client.get("/books")

    @task(1)
    def particular_book(self):
        # response != 2xx => failure
        # self.client.get("/books/1234")

        # manually controlling success/failure
        with self.client.get("/books/1234", catch_response=True) as response:
            if response.status_code == NOT_FOUND:
                response.failure("book not found") # response.success()


class WebsiteUser(HttpLocust):
    """ locust class """
    task_set = UserBehavior # references TaskSet class
    min_wait = 300 # wait ms between task execution for sim user
    max_wait = 1000
    host = "http://localhost:1234" # usually provided on command line, --host
    # use weight attribute with multiple locust classes
