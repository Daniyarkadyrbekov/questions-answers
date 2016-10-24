
from wsgiref.simple_server import make_server


def application(environ, start_response):
    def add_to_list(s: str, result_list: list):
        result_list.append(s.encode("utf-8"))

    result_list = list()
    add_to_list("Hello world!\n", result_list)
    for key in environ:
        add_to_list("%s: %s\n" % (key, str(environ[key])), result_list)

    print(environ.get)

    start_response("200 OK", [("Content-type", "text/plain")])
    #return ["Hello my friend!".encode("utf-8")]
    return result_list


server = make_server('localhost', 8081, application)
server.serve_forever()