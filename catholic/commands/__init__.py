import click

from catholic.commands.catechism import catechism


def register_commands(group: click.Group):
    group.add_command(catechism)
