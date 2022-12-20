import typer
from typing import List
from pathlib import Path
from base import convert_to_cbz

from rich.text import Text
from rich.console import Console

app = typer.Typer()


@app.command()
def convert(files: List[Path]):
    convert_to_cbz(files)


if __name__ == "__main__":
    app()
