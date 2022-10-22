import os
import pickle


def read_pickle(name: str) -> dict:
    """
    Reads pickles by name
    :param name:
    :return:
    """
    this_dir, _ = os.path.split(__file__)
    data_path = os.path.join(this_dir, name)
    with open(data_path, 'rb') as handle:
        return pickle.load(handle)
