from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello, World']

if __name__ == '__main__':
    server = make_server('', 8888, application)
    print("server running on port 8888")
    server.serve_forever()
