from pathlib import Path

import typer


def main(config: Path = typer.Option(...)):
    if config.is_file():
        text = config.read_text()
        typer.echo(f"Config file contents: {text}")
    elif config.is_dir():
        typer.echo("Config is a directory, will use all its config files")
    elif not config.exists():
        typer.echo("The config doesn't exist")


if __name__ == "__main__":
    typer.run(main)
