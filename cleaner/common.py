from cleaner import Cleaner

"""
通用清洗
"""


class TimeFormatCleaner(Cleaner):
    """
    时间格式化
    """

    def clean(self, origin):
        return origin[0:10]


class FillBlankCleaner(Cleaner):
    """
    空白填充
    """

    def __init__(self, *args):
        self.fill_data = args[0]

    def clean(self, origin):
        if not origin:
            return self.fill_data


class FillAllCleaner(Cleaner):
    """
    全量填充
    """

    def __init__(self, *args):
        self.fill_data = args[0]

    def clean(self, origin):
        return self.fill_data


class DictReplaceCleaner(Cleaner):
    """
    字典替换
    """

    def __init__(self, *args):
        self.dict = args[0]

    def clean(self, origin):
        if origin in self.dict:
            return self.dict[origin]
        else:
            if 'default' in self.dict:
                return self.dict['default']


class StripUuidCleaner(Cleaner):
    """
    截取UUID
    """

    def __init__(self, *args):
        self.length = args[0]

    def clean(self, origin):
        return origin.replace('-', '')[0:self.length]


class StripStringCleaner(Cleaner):
    """
    截取普通字符串
    """

    def __init__(self, *args):
        self.length = args[0]

    def clean(self, origin):
        return origin[0:self.length]
