import click

from catholic.commands.canon import canon
from catholic.commands.catechism import catechism
from catholic.commands.missal import missal


def register_commands(group: click.Group):
    group.add_command(cmd=catechism, name="catechism")
    group.add_command(cmd=canon, name="canon")
    group.add_command(cmd=missal, name="missal")
