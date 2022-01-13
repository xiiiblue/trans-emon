import random

from faker import Faker
from cleaner import CellCleaner

"""
数据模拟
"""

faker = Faker("zh_CN")


class MockAddressCleaner(CellCleaner):
    """
    模拟姓名
    """

    def clean(self, origin=None):
        return faker.address()


class MockCityCleaner(CellCleaner):
    """
    模拟城市
    """

    def clean(self, origin=None):
        return faker.city()


class MockZipCodeCleaner(CellCleaner):
    """
    模拟邮编
    """

    def clean(self, origin=None):
        return faker.postcode()


class MockNameCleaner(CellCleaner):
    """
    模拟姓名
    """

    def clean(self, origin=None):
        return faker.name()


class MockCompanyCleaner(CellCleaner):
    """
    模拟公司名
    """

    def clean(self, origin=None):
        return faker.company()


class MockPhoneCleaner(CellCleaner):
    """
    模拟电话号码
    """

    def clean(self, origin=None):
        return faker.phone_number()


class MockIdCardCleaner(CellCleaner):
    """
    模拟身份证
    """

    def clean(self, origin=None):
        return faker.ssn()


class MockSentenceCleaner(CellCleaner):
    """
    模拟文本
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[0], int):
                self.sentence_number = args[0]
            else:
                raise RuntimeError('自增序列参数必须是数字')
        else:
            self.sentence_number = 1

    def clean(self, origin=None):
        sentences = faker.paragraph(nb_sentences=self.sentence_number, variable_nb_sentences=True)
        if self.sentence_number == 1:
            return sentences.replace('.', '')
        else:
            return sentences


class MockNumberCleaner(CellCleaner):
    """
    模拟数字
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[0], int):
                self.min = args[0]
                self.max = args[1]
            else:
                raise RuntimeError('自增序列参数必须是数字')
        else:
            self.min = 0
            self.max = 999999

    def clean(self, origin=None):
        return random.randint(self.min, self.max)


if __name__ == '__main__':
    cleaner = MockNumberCleaner()
    print(cleaner.clean())
