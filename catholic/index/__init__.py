import os

from whoosh import index
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


def write_catechism_data_to_index(data, writer):
    for d in data:
        writer.add_document(id=str(d["id"]).encode("utf-8").decode("utf-8"), text=str(d["text"]))
    writer.commit()


def write_missal_data_to_index(data, writer):
    for d in data:
        writer.add_document(id=str(d["id"]).encode("utf-8").decode("utf-8"), text=str(d["text"]))
    writer.commit()


def write_canon_data_to_index(data, writer):
    for d in data:
        text = ""
        if "text" in d:
            text = str(d["text"])
        elif "sections" in d:
            for s in d["sections"]:
                text += str(s["text"] + " ")
        writer.add_document(id=str(d["id"]).encode("utf-8").decode("utf-8"), text=text)
    writer.commit()


def create_index(index_dir, schema, write_to_index_func, data):
    # create empty index directory
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    # we will use the schema to initialize a Whoosh index in the above directory.
    ix = index.create_in(index_dir, schema)
    writer = ix.writer()

    # Lastly, let us fill this index with the data from the catechism data.
    write_to_index_func(data, writer)
