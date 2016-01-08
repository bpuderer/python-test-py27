from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from urlparse import urlparse, parse_qs
import argparse
import os
import subprocess
import json

def duplicate_book(newbk):
    #duplicate if book exists with same ISBN-10 identifier
    for book in books['books']:
        if book['identifier']['ISBN-10'] == newbk['identifier']['ISBN-10']:
            return True
    return False

class HttpSim(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed_path = urlparse(self.path)

        if parsed_path.path == "/terminate":
            self.send_response(200)
            subprocess.call(["kill", str(os.getpid())])
        elif parsed_path.path == "/books":
            response_body = json.dumps(books)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(response_body))
            self.end_headers()
            self.wfile.write(response_body)
        else:
            self.send_error(404)
        return


    def do_POST(self):

        content_len = int(self.headers.getheader('content-length', 0))
        if content_len:
            request_body = self.rfile.read(content_len)
        else:
            self.send_error(400, "no Content-Length header found and this sim does not handle chunked transfer encoding")
            return

        parsed_path = urlparse(self.path)
        if parsed_path.path == "/books":
            #assumes valid json in request body
            new_book = json.loads(request_body)
            if not duplicate_book(new_book):
                books['books'].append(new_book)
                self.send_response(201)
            else:
                self.send_error(409)
        else:
            self.send_error(404)
        return


    def do_PUT(self):
        self.send_error(404)
        return


    def do_DELETE(self):

        parsed_path = urlparse(self.path)
        if parsed_path.path == "/books":
            #delete all
            del books['books'][:]
            self.send_response(200)
        else:
            self.send_error(404)
        return


class ThreadedHttpSim(ThreadingMixIn, HTTPServer):
    """multithread"""

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="localhost")
    parser.add_argument("--port", type=int, default="1234")
    args = parser.parse_args()
    IP = args.ip
    PORT = args.port

    books = {'books': []}

    try:
        server = ThreadedHttpSim((IP, PORT), HttpSim)
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
