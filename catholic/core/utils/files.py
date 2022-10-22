import os
import pickle

from pickles import read_pickle


def load_pickle(pickle_name: str):
    """
    TIP: DO NOT use this
    Reads the contents of the given pickle, and returns a dict.
    :param pickle_name: Name of the pickle file
    :return: dict
    """
    with open(pickle_name, 'rb') as handle:
        return pickle.load(handle)


def load_pickle_by_name(name: str):
    """
    Reads the contents of the given pickle, and returns a dict.
    :param name: Name of the pickle file
    :return: dict
    """
    return read_pickle(name)
