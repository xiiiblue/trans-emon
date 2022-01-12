import uuid

from processor import Processor


class TimeFormatProcessor(Processor):
    """
    时间格式化
    """

    def process(self, origin):
        return origin[0:10]


class FillBlankProcessor(Processor):
    """
    空白填充
    """

    def __init__(self, *args):
        self.fill_data = args[0]

    def process(self, origin):
        if not origin:
            return self.fill_data


class FillAllProcessor(Processor):
    """
    全量填充
    """

    def __init__(self, *args):
        self.fill_data = args[0]

    def process(self, origin):
        return self.fill_data


class DictProcessor(Processor):
    """
    全量填充
    """

    def __init__(self, *args):
        self.dict = args[0]

    def process(self, origin):
        if origin in self.dict:
            return self.dict[origin]
        else:
            if 'default' in self.dict:
                return self.dict['default']


class UuidProcessor(Processor):
    """
    UUID填充
    """

    def __init__(self, *args):
        self.length = args[0]

    def process(self, origin):
        return str(uuid.uuid4()).replace('-', '')[0:self.length]
