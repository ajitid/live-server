import os.path
import os

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.autoreload

from . import global_vars
from .inject import inject_live_server_script


class HtmlHandler(tornado.web.RequestHandler):
    def initialize(self, path, default_filename=None):
        self.root = path
        self.default_filename = default_filename

    def get(self, captured):
        if captured is None:
            captured = self.default_filename
        try:
            injected_html = inject_live_server_script(
                os.path.join(self.root, captured))
            self.write(injected_html)
        except FileNotFoundError:
            self.send_error(404)


class LiveServerHandler(tornado.websocket.WebSocketHandler):
    active_clients = set()

    def open(self):
        LiveServerHandler.active_clients.add(self)

    def on_close(self):
        LiveServerHandler.active_clients.remove(self)


def broadcast_reload():
    for client in LiveServerHandler.active_clients:
        client.write_message('reload', binary=False)


def make_app():
    STATIC_PATH = global_vars.PATH

    LIVE_SERVER_JS_PATH = os.path.join(os.path.dirname(__file__))
    config = {
        'debug': True,
        'serve_traceback': False
    }
    static_config = {'path': STATIC_PATH, 'default_filename': 'index.html'}

    return tornado.web.Application([
        (r'/(.*\.html)?', HtmlHandler, static_config),
        (r'/ws/live-server', LiveServerHandler),
        (r'/(liveServer.js)', tornado.web.StaticFileHandler,
         {'path': LIVE_SERVER_JS_PATH}),
        (r'/(.*)', tornado.web.StaticFileHandler, static_config)
    ], **config)


def start_app():
    app = make_app()
    server = app.listen(global_vars.PORT)
    print('listening on {}'.format(global_vars.PORT))
    return server


def stop_app(app):
    app.stop()
