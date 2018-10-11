import click

import global_vars
import watcher


@click.command()
@click.option('--port', '-P', default=8888, help='Port to use to serve website.')
@click.option('--path', '-p', default='.', help='Relative path to the directory which should be served.')
def cli(port, path):
    global_vars.PORT = int(port)
    global_vars.PATH = path
    watcher.main()


if __name__ == '__main__':
    cli()
