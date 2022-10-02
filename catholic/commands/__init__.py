import click

from catholic.commands.canon_law import canon, cl
from catholic.commands.catechism import catechism, c
from catholic.commands.roman_missal import missal, m


def register_commands(group: click.Group):
    group.add_command(catechism)
    group.add_command(c)
    group.add_command(canon)
    group.add_command(cl)
    group.add_command(missal)
    group.add_command(m)

