import click
from pyror import ror_match


@click.command()
@click.option("--name", help="university name")
def ror(name):
    """Get a ROR ID (as a URI) from an institution name
    
    Search for ror id's by an institution's name
    
    ror --name 'University of California, Berkeley'
    """
    res = ror_match(name=name)
    click.echo(click.style(f"institution searched: {name}", fg="green"))
    if isinstance(res, dict):
        res = res["id"]
        click.echo(click.style(res, fg="magenta"))
    else:
        click.echo(click.style("more than one match found", fg="green"))
        for uni in res:
            click.echo(click.style("  " + uni["id"], fg="magenta"))
