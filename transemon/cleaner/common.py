from transemon.cleaner import CellCleaner

"""
通用清洗
"""


class TimeFormatCleaner(CellCleaner):
    """
    时间格式化
    """

    def clean(self, origin=None):
        return origin[0:10]


class FillBlankCleaner(CellCleaner):
    """
    空白填充
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            self.fill_data = args[0]
        else:
            self.fill_data = '***'

    def clean(self, origin=None):
        if not origin:
            return self.fill_data


class FillAllCleaner(CellCleaner):
    """
    全量填充
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            self.fill_data = args[0]
        else:
            self.fill_data = '***'

    def clean(self, origin=None):
        return self.fill_data


class DictReplaceCleaner(CellCleaner):
    """
    字典替换
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            self.dict = args[0]
        else:
            raise RuntimeError('字典替换参数未传入')

    def clean(self, origin=None):
        if origin in self.dict:
            return self.dict[origin]
        else:
            if 'default' in self.dict:
                return self.dict['default']
            else:
                return origin


class StripUuidCleaner(CellCleaner):
    """
    截取UUID
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            self.length = args[0]
        else:
            self.length = 16

    def clean(self, origin=None):
        return origin.replace('-', '')[0:self.length]


class StripStringCleaner(CellCleaner):
    """
    截取普通字符串
    """

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            self.length = args[0]
        else:
            self.length = 16

    def clean(self, origin=None):
        return origin[0:self.length]
