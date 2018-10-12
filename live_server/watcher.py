from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tornado.ioloop
import tornado.autoreload

from . import global_vars
from . import server

app = None
observer = None
loop = None


class LiveServerEventHandler(FileSystemEventHandler):
    def refresh_app():
        global app

        server.broadcast_reload()

    def on_any_event(self, event):
        global app
        global loop

        loop.add_callback(LiveServerEventHandler.refresh_app)


def watch():
    global observer

    live_server_event_handler = LiveServerEventHandler()
    observer = Observer()
    observer.schedule(live_server_event_handler,
                      global_vars.PATH, recursive=True)
    observer.start()


def main():
    global app
    global loop

    loop = tornado.ioloop.IOLoop.current()
    loop.add_callback(watch)
    app = server.start_app()
    try:
        loop.start()
    except KeyboardInterrupt:
        print('\nLive Server stopped.')
