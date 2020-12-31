import typer
import os
from sys import platform
from pathlib import Path
import src


app = typer.Typer()

username = os.path.expanduser('~').split('/')[-1]
kindle_path = Path(f'/media/{username}/Kindle/')


def main(destination: str, verbose: bool = False) -> None:
    """Syncronize your highlights from a connected Kindle device."""
    if not kindle_is_connected():
        return

    clippings_file = kindle_path / 'documents/My Clippings.txt'
    if not os.path.isfile(clippings_file):
        typer.echo('No clippings found on connected Kindle.')
        return

    klipings_lines = src.read_clippings(clippings_file)
    clippings = src.sort_clippings(klipings_lines)
    src.write_clippings(
        clippings,
        destination,
        verbose=verbose
    )


def kindle_is_connected() -> bool:


if __name__ == "__main__":
    typer.run(main)
