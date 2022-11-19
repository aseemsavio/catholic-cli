import os

from whoosh import index, qparser
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, ID, TEXT


def catechism_schema():
    return Schema(id=ID(stored=True),
                  text=TEXT(analyzer=StemmingAnalyzer())
                  )


def missal_schema():
    return Schema(id=ID(stored=True),
                  text=TEXT(analyzer=StemmingAnalyzer())
                  )


def canon_schema():
    return Schema(id=ID(stored=True),
                  text=TEXT(analyzer=StemmingAnalyzer())
                  )


def create_index(index_dir: str, schema, write_to_index_func, data):
    # create empty index directory
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    # we will use the schema to initialize a Whoosh index in the above directory.
    ix = index.create_in(index_dir, schema)
    writer = ix.writer()

    # Lastly, let us fill this index with the data from the catechism data.
    write_to_index_func(data, writer)


def _search(dir_name, search_fields, search_query) -> list:
    ix = index.open_dir(dir_name)
    schema = ix.schema

    # og = qparser.OrGroup.factory(0.9)
    mp = qparser.MultifieldParser(search_fields, schema)

    q = mp.parse(search_query)

    with ix.searcher() as s:
        return [int(r.fields()["id"]) for r in s.search(q, terms=True, limit=2000)]


def search_catechism(search_query: str):
    """
    Searches Catechism
    :param search_query: Query to search
    :return: IDs of the matched paragraphs
    """
    this_dir, _ = os.path.split(__file__)
    return _search(f"{this_dir}/catechism_index", ["text"], str(search_query))


def search_canon(search_query: str):
    """
    Searches Canon
    :param search_query: Query to search
    :return: IDs of the matched paragraphs
    """
    this_dir, _ = os.path.split(__file__)
    return _search(f"{this_dir}/canon_index", ["text"], str(search_query))


def search_missal(search_query: str):
    """
    Searches Missal
    :param search_query: Query to search
    :return: IDs of the matched paragraphs
    """
    this_dir, _ = os.path.split(__file__)
    return _search(f"{this_dir}/missal_index", ["text"], str(search_query))
