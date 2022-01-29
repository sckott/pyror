import click
from pyror import ror_match, ror_id


@click.command()
@click.option("--name", help="orgnization name")
@click.option("--id", help="orgnization id")
def ror(name, id):
    """Get a ROR ID (as a URI) from an orgnization name

    Search for ror id's by an orgnization's name

    ror --name 'University of California, Berkeley'

    ror --id 01an7q238
    """
    if id:
        res = ror_id(ror=id)
        if isinstance(res, dict):
            click.echo(click.style(f"ROR ID searched: {id}", fg="green"))
            click.echo(click.style(res["name"], fg="magenta"))
            click.echo(click.style(res["links"][0], fg="magenta"))
    else:
        res = ror_match(name=name)
        click.echo(click.style(f"orgnization searched: {name}", fg="green"))
        if isinstance(res, dict):
            res = res["id"]
            click.echo(click.style(res, fg="magenta"))
        else:
            click.echo(click.style("more than one match found", fg="green"))
            for uni in res:
                click.echo(click.style("  " + uni["id"], fg="magenta"))
