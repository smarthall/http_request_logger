#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)
# Alterations by Daniel Hall (2020)

from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from socket import gethostname

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):

        self.send_response(200)
        self.end_headers()

        message = (
        "Server: %s\n"
        "Request Path: %s\n"
        "--- START HEADERS ---\n"
        "%s\n"
        "--- END HEADERS ---\n"
        ) % (gethostname(), self.path, self.headers)

        self.wfile.write(b"<html><head><title>Echoserver</title></head><body><pre>")

        self.wfile.write(message.encode('utf-8'))

        self.wfile.write(b"</pre></body></html>")
        
    def do_POST(self):

        self.send_response(200)
        self.end_headers()

        message = (
        "Server: %s\n"
        "Request Path: %s\n"
        "--- START HEADERS ---\n"
        "%s\n"
        "--- END HEADERS ---\n"
        ) % (gethostname(), self.path, self.headers)

        self.wfile.write(b"<html><head><title>Echoserver</title></head><body><pre>")

        self.wfile.write(message.encode('utf-8'))

        self.wfile.write(b"</pre></body></html>")
    
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    port = 8080
    print('Listening on 0.0.0.0:%s' % port, flush=True)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will reflect headers back to the client\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
    main()
