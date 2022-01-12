from abc import abstractmethod


@abstractmethod
class Processor(object):
    """
    Excel处理策略
    """

    def __init__(self, *args):
        pass

    def process(self, origin):
        raise NotImplementedError
