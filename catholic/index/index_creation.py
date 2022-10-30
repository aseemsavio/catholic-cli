# There is no need to run this file unless there is a specific need to.

from catholic.core.utils.files import load_pickle_by_name
from catholic.index import create_index, catechism_schema, write_catechism_data_to_index, missal_schema, \
    write_missal_data_to_index, canon_schema, write_canon_data_to_index


def create_indices_for_catholic_data():
    create_index("catechism_index",
                 catechism_schema(),
                 write_catechism_data_to_index,
                 load_pickle_by_name("catechism.pickle"))

    create_index("missal_index",
                 missal_schema(),
                 write_missal_data_to_index,
                 load_pickle_by_name("girm.pickle"))

    create_index("canon_index",
                 canon_schema(),
                 write_canon_data_to_index,
                 load_pickle_by_name("canon.pickle"))


create_indices_for_catholic_data()
