# coding: utf-8

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from chatbot.test_chatbot import get_response, init_chatbot
import cgi
import demjson

# http.server不建议生产环境使用

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
        # ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        # if ctype == 'multipart/form-data':
        #     postvars = cgi.parse_multipart(self.rfile, pdict)
        # elif ctype == 'application/x-www-form-urlencoded':
        #     length = int(self.headers.getheader('content-length'))
        #     postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        # else:
        #     postvars = {}

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
