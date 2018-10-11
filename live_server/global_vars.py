import os

PORT = 8888
PATH = '.'


def get_resolved_path():
    global PATH
    resolved_path = os.getcwd()
    if PATH != '.':
        resolved_path = os.path.join(os.getcwd(), PATH)
    return resolved_path
