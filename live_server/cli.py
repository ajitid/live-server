import click

from . import global_vars
from . import watcher


@click.command()
@click.version_option()
@click.option('--port', '-p', default=8888, help='Port to use to serve website.')
@click.argument('path', default='.', type=click.Path(exists=True, dir_okay=True, readable=True, resolve_path=True))
def cli(port, path):
    global_vars.PORT = int(port)
    global_vars.PATH = path
    try:
        watcher.main()
    except OSError:
        print('Port {} is already in use. Use `-P` flag and specify a different port.'.format(global_vars.PORT))


if __name__ == '__main__':
    cli()
