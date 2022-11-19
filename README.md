# 🇻🇦catholic-cli

[![Catholic CLI](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/aseemsavio/catholic-cli)

The `catholic-cli` is the Swiss Army Knife Command Line Utility for quickly accessing
Catholic information. The tool currently has the following functionalities:

1. Access information from **The Catechism** of The Catholic Church,
2. Access information from **The Roman Missal**,
3. Access Information from **The Canon Law** of The Catholic Church

### General Syntax

The general syntax for using the tool is as follows.

```
<command> <sub-command> <options>
```

The default command in this CLI is `catholic`. All the sub commands are grouped under it.

The allowed sub-commands are:

1. `catechism`
2. `missal`
3. `canon`

The options currently supported by the `catholic-cli` are:

|     | Option        | Short Form | Data Type | Description                             | Commands/sub-commands that allow this option | Examples                                                                      |
|-----|---------------|------------|-----------|-----------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------|
| 1   | `--paragraph` | `--p`      | INT, TEXT | Displays Paragraph(s) with the given ID | `catechism`<br/>`canon`<br/>`missal`         | `--paragraph 10`<br/>`--p 10`<br/> `--p 1-5`<br/>`--p 1,2`<br/> `--p 1,2,4-5` |
| 2   | `--search`    | `--s`      | TEXT      | Search for the given string             | `catechism`<br/>`canon`<br/>`missal`         | `--search "Christ"`<br/>`--s "eucharist"`<br/>`--s "The Church"`              |
| 3   | `--help`      |            | BOOLEAN   | Get help text                           | `catholic`                                   | `--help`                                                                      |
| 4   | `--version`   |            | BOOLEAN   | Displays the version of this CLI        | `catholic`                                   | `--version`                                                                   |

