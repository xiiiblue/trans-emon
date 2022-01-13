from abc import abstractmethod


@abstractmethod
class Cleaner(object):
    """
    Excel处理策略
    """

    def __init__(self, *args):
        pass

    def clean(self, origin=None):
        raise NotImplementedError
