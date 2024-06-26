from transemon.cleaner import CellCleaner

"""
检查清单
"""


class CheckListCleaner(CellCleaner):

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            self.check_list = args[0]
        else:
            raise RuntimeError('清单标记必须传入一个List')

    def clean(self, origin=None):
        if origin in self.check_list:
            return '请核查'
