import click

from catholic.commands.canon_law import canon
from catholic.commands.catechism import catechism, c
from catholic.commands.roman_missal import missal


def register_commands(group: click.Group):
    group.add_command(catechism)
    group.add_command(c)
    group.add_command(canon)
    group.add_command(missal)
