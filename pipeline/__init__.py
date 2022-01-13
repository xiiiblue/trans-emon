from abc import abstractmethod
from settings import CLEANER

"""
流水线
"""


class Pipeline(object):

    @abstractmethod
    def process(self):
        raise NotImplementedError

    @staticmethod
    def get_cleaner(method, *args):
        """
        获取清洗器实例
        """
        if method not in CLEANER:
            raise RuntimeError('数据清洗器不存在')

        return CLEANER[method][0](*args)

    @staticmethod
    def get_method_name(method):
        """
        获取清洗规则名称
        """
        if method not in CLEANER:
            raise RuntimeError('数据清洗器不存在')

        return CLEANER[method][1]
