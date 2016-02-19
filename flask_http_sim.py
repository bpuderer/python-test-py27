import argparse
from flask import Flask, request, jsonify, abort
app = Flask(__name__)

library = {'books': []}


def book_location(isbn10):
    for i, book in enumerate(library['books']):
        if book['identifier']['ISBN-10'] == isbn10:
            return i
    return -1


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(library)

@app.route('/books/<bookid>', methods=['GET'])
def get_book(bookid):
    loc = book_location(bookid)
    if loc > -1:
        return jsonify(library['books'][loc])
    else:
        abort(404)

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json:
        abort(400)
    elif 'identifier' not in request.json or 'ISBN-10' not in request.json['identifier'] or 'title' not in request.json:
        abort(400)
    elif type(request.json['identifier']['ISBN-10']) != unicode or type(request.json['title']) != unicode:
        abort(400)
    elif not request.json['identifier']['ISBN-10'].strip() or not request.json['title'].strip():
        abort(400)
    elif book_location(request.json['identifier']['ISBN-10']) > -1:
        abort(409)
    else:
        library['books'].append(request.json)
        return jsonify(request.json), 201

@app.route('/books', methods=['DELETE'])
def delete_books():
    del library['books'][:]
    return ('', 200)

@app.route('/books/<bookid>', methods=['DELETE'])
def delete_book(bookid):
    loc = book_location(bookid)
    if loc > -1:
        del library['books'][loc]
        return ('', 200)
    else:
        abort(404)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="localhost")
    parser.add_argument("--port", type=int, default="1234")
    args = parser.parse_args()
    IP = args.ip
    PORT = args.port

    app.run(host=IP, port=PORT, debug=True)
