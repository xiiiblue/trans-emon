import random

from faker import Faker
from cleaner import Cleaner

"""
数据模拟
"""


class MockAddressCleaner(Cleaner):
    """
    模拟姓名
    """

    def __init__(self, *args):
        self.faker = Faker("zh_CN")

    def clean(self, origin=None):
        return self.faker.address()


class MockCityCleaner(Cleaner):
    """
    模拟城市
    """

    def __init__(self, *args):
        self.faker = Faker("zh_CN")

    def clean(self, origin=None):
        return self.faker.city()


class MockZipCodeCleaner(Cleaner):
    """
    模拟邮编
    """

    def __init__(self, *args):
        self.faker = Faker("zh_CN")

    def clean(self, origin=None):
        return self.faker.postcode()


class MockNameCleaner(Cleaner):
    """
    模拟姓名
    """

    def __init__(self, *args):
        self.faker = Faker("zh_CN")

    def clean(self, origin=None):
        return self.faker.name()


class MockCompanyCleaner(Cleaner):
    """
    模拟公司名
    """

    def __init__(self, *args):
        self.faker = Faker("zh_CN")

    def clean(self, origin=None):
        return self.faker.company()


class MockPhoneCleaner(Cleaner):
    """
    模拟电话号码
    """

    def __init__(self, *args):
        self.faker = Faker("zh_CN")

    def clean(self, origin=None):
        return self.faker.phone_number()


class MockIdCardCleaner(Cleaner):
    """
    模拟身份证
    """

    def __init__(self, *args):
        self.faker = Faker("zh_CN")

    def clean(self, origin=None):
        return self.faker.ssn()


class MockSentenceCleaner(Cleaner):
    """
    模拟文本
    """

    def __init__(self, *args):
        self.faker = Faker("zh_CN")

    def clean(self, origin=None):
        return self.faker.paragraph(nb_sentences=3, variable_nb_sentences=True)


class MockNumberCleaner(Cleaner):
    """
    模拟数字
    """

    def __init__(self, *args):
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
