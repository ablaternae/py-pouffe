# =============================================================================
#
# =============================================================================


import os
from multiprocessing import Process

import click

from .. import options
from ..__about__ import *
from ..http import server


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
    help=summary(),
)
@click.option("-r", "--start", is_flag=True, default=False, help="Server run")
@click.option(
    "-d",
    "--data-dir",
    # is_flag=True,
    default=options.STORAGE_DATA_DIR,
    type=click.Path(exists=False),
    help=f"Data directory, default `{options.STORAGE_DATA_DIR}`",
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
    default=str(options.HTTP_HOST),
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
    admin_panel=None,
    data_dir=None,
    host=None,
    port=None,
    start=None,
    engine=None,
):
    if admin_panel:
        options.HTTP_ADMIN_PANEL = admin_panel

    if data_dir:
        data_dir = os.path.realpath(data_dir)
        # options.STORAGE_DATA_DIR = data_dir
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

    if start:
        # print(summary())
        print("Server start...")
        print("Version", __version__)
        print("Id", __id__)

        try:
            proc = Process(
                target=server.start,
                name="process_http_server",
                kwargs=dict(host=host, port=port),
            )
            proc.start()
            proc.join()
        except KeyboardInterrupt as exc:
            print("Keyboard Interrupt detected")

        print("Server stop")

    return
