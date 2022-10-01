import click


@click.command()
@click.pass_context
def canon(ctx: click.Context):
    print("Canon Law")
