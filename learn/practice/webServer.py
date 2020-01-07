from wsgiref.simple_server import make_server

def application(environ, start_response):

    status = '200 OK'

    response_headers = [('Content-type', 'text/html')]

    start_response(status, response_headers)

    body = 'Hello, {name} !!!'.format(name=environ['PATH_INFO'][1:] or 'WSGI')

    return [body.encode('utf-8')]


app = make_server('', 8000, application)

app.serve_forever()