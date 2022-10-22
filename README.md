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
catholic <resource> <options>
```

A resource is either `catechism`, or `canon` or `missal`. An example for an option would be
`--paragraph` or it's shortform `--p`. You give values for an option like so: `--p 101`, where `101` is the value passed
to the option `--p`.

The allowed options are as follows.

| Option        | Short Form | Description                                                                                               | Examples                                                                                                                                    | 
|---------------|------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `--paragraph` | `--p`      | To Query Paragraphs                                                                                       | `--paragraph 101` <br/> `--paragraph 1,2` <br/> `--paragraph 1,2,6-10` <br/> `--p 101` <br/> `--p 101` <br/> `--p 1,2` <br/> `--p 1,2,6-10` |   
| `--search`    | `--s`      | To Look Up a given search string in Catechism / Canon / Missal.  <br/>  <br/> This is not case sensitive. | `--search "Christ"` <br/> `--s "Christ The King"`                                                                                           |   

The following command gives you paragraph 101 of the Catechism.

```
catholic catechism --p 101
```

The option `--p` or `--paragraph` takes in an integer (`101`) or a query string (`1,2,3-6` or `1,2` or `3-5`).
The query string can be a comma separated integers and, or ranges. For example:

```
catholic catechism --p 1,2,4-6
```

The above query would display paragraphs 1, 2, 4, 5, and 6. If you intend to add spaces in the query string, you may
do so within double quotes as follows.

```
catholic catechism --p "1, 2, 4 - 6"
```

Here are some example commands.

### Catechism

```
catholic catechism --paragraph 101
```

The tool also allows a short form for power users.

```
catholic c --p 101
```

You can provide a query string _instead of_ an integer to `--p` or `--paragraph` like so:

```
catholic catechism --p 1,2,4-6
```

You can search the Catechism for words or phrases like so. The short form `--s` can be used
instead of `--search`.

```
catholic catechism --search eucharist
```

For searching phrases that include spaces, they must be included within quotes.

```
catholic c --s "child of"
```

### Roman Missal

```
catholic missal --p 101
```

Shortform for the same would be:

```
catholic m --p 101
```

You can query the Missal like so:

```
catholic missal --p 1,2,3,77-79
```

You can search the Missal for words or phrases like so. The short form `--s` can be used
instead of `--search`.

```
catholic missal --search eucharist
```

For searching phrases that include spaces, they must be included within quotes.

```
catholic m --s "child of"
```

### Canon Law

```
catholic canon --p 101
```

Shortform for the same would be:

```
catholic cl --p 101
```

You can query the Canon Law like so:

```
catholic canon --p 1,2,3,77-79
```

You can search the Canon Law for words or phrases like so. The short form `--s` can be used
instead of `--search`.

```
catholic canon --search eucharist
```

For searching phrases that include spaces, they must be included within quotes.

```
catholic cl --s "child of"
```
