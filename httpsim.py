from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from urlparse import urlparse
import argparse
import os
import subprocess
import json
import re


def book_location(isbn10):
    for i, book in enumerate(library['books']):
        if book['identifier']['ISBN-10'] == isbn10:
            return i
    return -1


class HttpSim(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed_path = urlparse(self.path)

        if parsed_path.path == "/terminate":
            self.send_response(200)
            subprocess.call(["kill", str(os.getpid())])
        elif parsed_path.path == "/books" or parsed_path.path == "/books/":
            response_body = json.dumps(library)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(response_body))
            self.end_headers()
            self.wfile.write(response_body)
        elif re.match(r'/books/\S+', parsed_path.path):
            #split takes care of trailing slash
            loc = book_location(parsed_path.path.split('/')[2])
            if loc > -1:
                response_body = json.dumps(library['books'][loc])
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", len(response_body))
                self.end_headers()
                self.wfile.write(response_body)
            else:
                self.send_error(404, "Book not found")
        else:
            self.send_error(404)
        return


    def do_POST(self):

        content_len = int(self.headers.getheader('content-length', 0))
        if content_len:
            request_body = self.rfile.read(content_len)
        else:
            #chunked transfer encoding not handled
            self.send_error(400, "non-zero Content-Length header not found")
            return

        parsed_path = urlparse(self.path)
        if parsed_path.path == "/books" or parsed_path.path == "/books/":
            try:
                new_book = json.loads(request_body)
                if ('identifier' not in new_book or 'ISBN-10' not in new_book['identifier'] or
                        'title' not in new_book or not new_book['identifier']['ISBN-10'].strip() or
                        not new_book['title'].strip()):
                    self.send_error(400, "Required field missing or has invalid value")
                elif book_location(new_book['identifier']['ISBN-10']) > -1:
                    self.send_error(409, "Book exists with passed ISBN-10")
                else:
                    library['books'].append(new_book)
                    self.send_response(201)
            except (ValueError, TypeError, AttributeError):
                self.send_error(400, "Error parsing JSON")
        else:
            self.send_error(404)
        return


    def do_DELETE(self):

        parsed_path = urlparse(self.path)
        if parsed_path.path == "/books" or parsed_path.path == "/books/":
            #delete all
            del library['books'][:]
            self.send_response(200)
        elif re.match(r'/books/\S+', parsed_path.path):
            #split takes care of trailing slash
            loc = book_location(parsed_path.path.split('/')[2])
            if loc > -1:
                del library['books'][loc]
                self.send_response(200)
            else:
                self.send_error(404, "Book not found")
        else:
            self.send_error(404)
        return


    def do_HEAD(self):

        parsed_path = urlparse(self.path)
        if parsed_path.path == "/books" or parsed_path.path == "/books/":
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

    library = {'books': []}

    try:
        server = ThreadedHttpSim((IP, PORT), HttpSim)
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
