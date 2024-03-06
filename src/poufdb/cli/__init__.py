# =============================================================================
#
# =============================================================================


import os
from multiprocessing import Process

import click

from poufdb import options
from poufdb.__about__ import *


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
    # help="Show this message and exit",
)
@click.option("-r", "--start", is_flag=True, default=False, help="API REST Server run")
@click.option(
    "-d",
    "--data-dir",
    # is_flag=True,
    default=options.DATA_DIR,
    type=click.Path(exists=False),
    help=f"Data directory, default `{options.DATA_DIR}`",
)
@click.option(
    "-a",
    "--admin-panel",
    is_flag=True,
    help="Start discrete server for admin panel (disable now)",
)
@click.option(
    "--host",
    # is_flag=True,
    default=int(options.HTTP_PORT),
    type=str,
    help=f"Host, default `{options.HTTP_HOST}`",
)
@click.option(
    "--port",
    # is_flag=True,
    default=int(options.HTTP_PORT),
    type=int,
    help=f"Port, default `{options.HTTP_PORT}`",
)
@click.option(
    "--engine",
    # is_flag=True,
    default="sqlite",
    type=click.Choice(["sqlite", "inmemory", "csv"]),
    help=f"Backend engine (disable now)",
)
@click.version_option(
    # version=__version__,
    __version__,
    "-v",
    "--version",
    # param_decls=['-v', '--version'],
    help="Show the version and exit",
    is_flag=True,
    prog_name="PoufDB",
)
def main(
    admin_panel=None, data_dir=None, host=None, port=None, start=None, engine=None
):

    if admin_panel:
        options.ADMIN_PANEL = admin_panel

    if data_dir:
        data_dir = os.path.realpath(data_dir)
        options.DATA_DIR = data_dir
        if not os.path.isdir(data_dir):
            try:
                os.mkdir(data_dir, 0o755)
                print(f"Creating directory `{data_dir}`... Ok")
            except:
                print(f"Creating directory `{data_dir}`... ERROR")

    if host:
        options.HTTP_HOST = host
    if port:
        options.HTTP_PORT = int(port)

    print(options.HTTP_PORT)

    if start:
        from ..http import server

        server.HTTP_PORT = options.HTTP_PORT
        print('server.HTTP_PORT', server.HTTP_PORT)
        print(__summary__)
        print("Server start...")
        print("Version", __version__)
        print("Id", __id__)

        try:
            proc = Process(target=server.start)
            proc.start()
            proc.join()
        except KeyboardInterrupt as exc:
            print("KeyboardInterrupt detected")

        print("Server stop")

    # print(admin_panel, data_dir, 755, 0x755, 0o755)
