import click
from pyror import fetch_id


@click.command()
@click.option("--name", help="university name")
def ror(name):
    """Get a ROR ID from an institution name"""
    id = fetch_id(name=name)
    click.echo(f"institution searched: {name}", fg="")
    click.echo(id, fg="")
