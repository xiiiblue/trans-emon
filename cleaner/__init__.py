from abc import abstractmethod


class Cleaner(object):
    """
    Excel处理策略
    """

    def __init__(self, *args):
        pass

    @abstractmethod
    def clean(self, origin=None):
        raise NotImplementedError
