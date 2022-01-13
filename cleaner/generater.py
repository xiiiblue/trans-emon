import random
import uuid

"""
数据生成
"""
from cleaner import Cleaner


class GenerateUuidCleaner(Cleaner):
    """
    生成UUID
    """

    def __init__(self, *args):
        self.length = args[0]

    def clean(self, origin):
        return str(uuid.uuid4()).replace('-', '')[0:self.length]


class GenerateRandomNumberCleaner(Cleaner):
    """
    生成随机数
    """

    def __init__(self, *args):
        self.length = args[0]

    def clean(self, origin):
        random_string = ""
        for i in range(self.length):
            random_string += chr(random.randrange(ord('0'), ord('9') + 1))
        return random_string


class GenerateSequenceCleaner(Cleaner):
    """
    生成自增序列
    """

    def __init__(self, *args):
        if args[0]:
            if not isinstance(args[0], int):
                raise RuntimeError('自增序列参数必须是数字')
            self.start_with = args[0]
        else:
            self.start_with = 1

        self.sequence = self.start_with - 1

    def clean(self, origin):
        self.sequence += 1
        return self.sequence
