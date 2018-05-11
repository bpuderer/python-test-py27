import time

import grpc
from locust import Locust, TaskSet, events, task

from doubler_pb2 import Number
import doubler_pb2_grpc


class UserBehavior(TaskSet):

    @task
    def make_call(self):
        """ tests grpc-demo/doubler/server.py """

        start_time = time.time()
        try:
            self.client.Double(Number(value=3.0), timeout=1)
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
