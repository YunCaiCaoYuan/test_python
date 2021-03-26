# coding: utf-8

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from chatbot.test_chatbot import get_response, init_chatbot
import demjson


# data = {'result': 'this is a test'}

host = ('localhost', 8888)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        res = get_response(chat_bot)
        data = {"result": str(res)}
        print("data=", data)
        self.wfile.write(json.dumps(data).encode())
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        res = get_response(chat_bot)
        data = {"result": str(res)}
        print("data=", data)
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    chat_bot = init_chatbot()

    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
