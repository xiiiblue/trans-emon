import random
import uuid
from transemon.cleaner import CellCleaner

"""
数据生成
"""


class GenerateUuidCleaner(CellCleaner):
    """
    生成UUID
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            if not isinstance(args[0], int):
                raise RuntimeError('UUID长度参数必须是数字')
            self.length = args[0]
        else:
            self.length = 16

    def clean(self, origin=None):
        return str(uuid.uuid4()).replace('-', '')[0:self.length]


class GenerateRandomNumberCleaner(CellCleaner):
    """
    生成随机数
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            if not isinstance(args[0], int):
                raise RuntimeError('随机数长度参数必须是数字')
            self.length = args[0]
        else:
            self.length = 16

    def clean(self, origin=None):
        random_string = ""
        for i in range(self.length):
            random_string += chr(random.randrange(ord('0'), ord('9') + 1))
        return random_string


class GenerateSequenceCleaner(CellCleaner):
    """
    生成自增序列
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            if not isinstance(args[0], int):
                raise RuntimeError('自增序列参数必须是数字')
            self.start_with = args[0]
        else:
            self.start_with = 1

        self.sequence = self.start_with - 1

    def clean(self, origin=None):
        self.sequence += 1
        return self.sequence
