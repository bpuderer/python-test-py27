import time

from grpc import insecure_channel
from google.protobuf import json_format
from locust import Locust, TaskSet, events, task
from locust.exception import LocustError

from grpc_request import doubler_pb2, doubler_pb2_grpc



class UserBehavior(TaskSet):

    def on_start(self):
        self.read_request()

    def read_request(self):
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


class GrpcLocust(Locust):
    def __init__(self):
        super(GrpcLocust, self).__init__()
        if self.host is None:
            raise LocustError("Host not specified")
        self.client = doubler_pb2_grpc.DoublerStub(insecure_channel(self.host))


class ApiUser(GrpcLocust):
    host = 'localhost:50051'
    task_set = UserBehavior
    min_wait = 300
    max_wait = 1000
