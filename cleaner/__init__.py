from abc import abstractmethod


class Cleaner(object):
    """
    清洗器
    """
    pass


class CellCleaner(Cleaner):
    """
    单元格清洗器
    """

    def __init__(self, *args):
        pass

    @abstractmethod
    def clean(self, origin=None):
        raise NotImplementedError


class RowCleaner(Cleaner):
    """
    行清洗器
    """

    def __init__(self, *args):
        pass

    @abstractmethod
    def load(self, origin_col_id, repository):
        raise NotImplementedError

    @abstractmethod
    def clean(self, row_id=None):
        raise NotImplementedError
