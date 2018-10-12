import click

from . import global_vars
from . import watcher


@click.group()
@click.version_option()
@click.option('--port', '-P', default=8888, help='Port to use to serve website.')
@click.option('--path', '-p', default='.', help='Relative path to the directory which should be served.')
def cli(port, path):
    global_vars.PORT = int(port)
    global_vars.PATH = path
    try:
        watcher.main()
    except OSError:
        print('Port {} is already in use. Use `-P` flag and specify a different port.'.format(global_vars.PORT))


if __name__ == '__main__':
    cli()
