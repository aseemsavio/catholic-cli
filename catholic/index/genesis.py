# There is no need to run this file unless there is a specific need to.

from catholic.core.utils.files import load_pickle_by_name
from catholic.index import create_index, catechism_schema, missal_schema, canon_schema, search


def _write_catechism_data_to_index(data, writer):
    for d in data:
        writer.add_document(id=str(d["id"]).encode("utf-8").decode("utf-8"), text=str(d["text"]))
    writer.commit()


def _write_missal_data_to_index(data, writer):
    for d in data:
        writer.add_document(id=str(d["id"]).encode("utf-8").decode("utf-8"), text=str(d["text"]))
    writer.commit()


def _write_canon_data_to_index(data, writer):
    for d in data:
        text = ""
        if "text" in d:
            text = str(d["text"])
        elif "sections" in d:
            for s in d["sections"]:
                text += str(s["text"] + " ")
        writer.add_document(id=str(d["id"]).encode("utf-8").decode("utf-8"), text=text)
    writer.commit()


def create_indices_for_catholic_data():
    create_index("catechism_index",
                 catechism_schema(),
                 _write_catechism_data_to_index,
                 load_pickle_by_name("catechism.pickle"))

    create_index("missal_index",
                 missal_schema(),
                 _write_missal_data_to_index,
                 load_pickle_by_name("girm.pickle"))

    create_index("canon_index",
                 canon_schema(),
                 _write_canon_data_to_index,
                 load_pickle_by_name("canon.pickle"))


# create_indices_for_catholic_data()

