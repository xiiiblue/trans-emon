from processor import Processor


class TimeFormatProcessor(Processor):
    """
    时间格式化
    """

    def process(self, origin):
        return origin[0:10]
