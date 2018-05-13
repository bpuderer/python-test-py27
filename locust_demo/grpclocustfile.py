""" locust demo for grpc service """

import time

from grpc import insecure_channel
from google.protobuf import json_format
from locust import Locust, TaskSet, events, task

from grpc_request import doubler_pb2, doubler_pb2_grpc


def report(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            func(*args, **kwargs)
        except Exception as ex:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="grpc", name=func.__name__,
                                        response_time=total_time, exception=ex)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="grpc", name=func.__name__,
                                        response_time=total_time, response_length=0)
    return wrapper


class UserBehavior(TaskSet):

    @task
    @report
    def double(self):
        self.client.Double(self.locust.request, timeout=1)

    @task
    @report
    def another_double(self):
        self.client.AnotherDouble(self.locust.request, timeout=1)


class GrpcLocust(Locust):
    def __init__(self):
        super(GrpcLocust, self).__init__()
        self.client = doubler_pb2_grpc.DoublerStub(insecure_channel(self.host))
        with open("./grpc_request/request.json") as infile:
            json_str = infile.read()
        self.request = json_format.Parse(json_str, doubler_pb2.Number())


class ApiUser(GrpcLocust):
    host = 'localhost:50051'
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 5000
