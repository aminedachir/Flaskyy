from werkzeug.wrappers import Request, Response

@Request.application
def hello(request):
    return Response('Hello World!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 9527, hello)