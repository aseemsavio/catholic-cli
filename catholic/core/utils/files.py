from catholic.pickles import read_pickle


def load_pickle_by_name(name: str):
    """
    Reads the contents of the given pickle, and returns a dict.
    :param name: Name of the pickle file
    :return: dict
    """
    return read_pickle(name)
