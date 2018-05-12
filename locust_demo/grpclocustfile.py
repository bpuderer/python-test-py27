import time

import grpc
from google.protobuf import json_format
from locust import Locust, TaskSet, events, task

from grpc_request import doubler_pb2, doubler_pb2_grpc


class UserBehavior(TaskSet):

    def on_start(self):
        with open("./grpc_request/request.json") as f:
            json_str = f.read()
        self.request = json_format.Parse(json_str, doubler_pb2.Number())

    @task
    def make_call(self):
        """ tests grpc-demo/doubler/server.py """

        start_time = time.time()
        try:
            self.client.Double(self.request, timeout=1)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="grpc", name="doubler", response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="grpc", name="doubler", response_time=total_time, response_length=0)


class GrpcUser(Locust):

    task_set = UserBehavior
    min_wait = 300
    max_wait = 1000

    channel = grpc.insecure_channel('localhost:50051')
    client = doubler_pb2_grpc.DoublerStub(channel)