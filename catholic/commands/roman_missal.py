import click


@click.command()
@click.pass_context
def missal(ctx: click.Context):
    print("Roman Missal")
