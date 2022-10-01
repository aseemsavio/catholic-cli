import pickle


def load_pickle(pickle_name: str):
    """
    Reads the contents of the given pickle, and returns a dict.
    :param pickle_name: Name of the pickle file
    :return: dict
    """
    with open(pickle_name, 'rb') as handle:
        return pickle.load(handle)
