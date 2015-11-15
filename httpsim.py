from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from urlparse import urlparse, parse_qs
import argparse
import time
import logging
import logging.handlers
import os
import subprocess
import json


class HttpSim(BaseHTTPRequestHandler):

    # if do_METHOD(self): not included below, sim responds with
    # 501 Unsupported method

    def do_GET(self):

        parsed_path = urlparse(self.path)

        query_fields = parse_qs(parsed_path.query)
        my_logger.info("Fields parsed from query string: " + str(query_fields)) 

        if parsed_path.path == "/terminate":
            my_logger.info("Client terminated the simulator")
            self.send_response(200)
            subprocess.call(["kill", str(os.getpid())])
        else:
            canned_book = {'identifier': {'ISBN-10': "0374530637", 'ISBN-13': "978-0374530631", 'OCLC': "256887668"}, 'title': "Wise Blood", 'pages': 238, 'available': True, 'authors': ["Flannery O'Connor"]}
            response_body = json.dumps(canned_book)
            self.send_response(200)
            self.send_header("Content-Type", "application_json")
            self.send_header("Content-Length", len(response_body))
            self.end_headers()
            self.wfile.write(response_body)
            my_logger.debug("Sent response to GET request: " + response_body)
            return

    def do_POST(self):

        content_len = int(self.headers.getheader('content-length', 0))
        if content_len:
            request_body = self.rfile.read(content_len)
            my_logger.debug("Received POST with message body: " + request_body)
            self.send_response(201)
            return
        else:
            self.send_error(400, "no Content-Length header found and this sim does not handle chunked transfer encoding")
            return

    def do_PUT(self):
        self.send_error(404)
        return

    def do_DELETE(self):
        self.send_error(404)
        return


class ThreadedHttpSim(ThreadingMixIn, HTTPServer):
    """multithread"""

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", dest="ip", default="localhost")
    parser.add_argument("--port", dest="port", type=int, default="1234")
    args = parser.parse_args()
    IP = args.ip
    PORT = args.port

    #setup rotating log file, (3) 1 MB files
    #nohup <start script with options> >/dev/null 2>&1 &
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler('httpsim.log', maxBytes=1048576, backupCount=3)
    handler.setLevel(logging.DEBUG)
    logging.Formatter.converter = time.gmtime
    #log format: timestamp|log level|thread id|message
    formatter = logging.Formatter('%(asctime)s.%(msecs)03dZ|%(levelname)s|%(thread)d|%(message)s', '%Y-%m-%dT%H:%M:%S')
    handler.setFormatter(formatter)
    my_logger.addHandler(handler)

    try:
        server = ThreadedHttpSim((IP, PORT), HttpSim)
        my_logger.info("Started httpsim")
        server.serve_forever()
    except KeyboardInterrupt:
        my_logger.info("^C received, stopping server")
        server.server_close()
