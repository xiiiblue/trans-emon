from dateutil import parser

from cleaner import RowCleaner

"""
日期比较
"""


class DateCompareCleaner(RowCleaner):

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            self.col_name_a = args[0]
            self.col_name_b = args[1]
        else:
            raise RuntimeError('日期比较必须传入两个列名')

    def load(self, origin_col_id, repository):
        """
        预处理
        """
        self.origin_col_id = origin_col_id
        self.repository = repository

        # 取两列ID
        self.col_id_a = self.repository.get_col_by_title(self.col_name_a)
        self.col_id_b = self.repository.get_col_by_title(self.col_name_b)

    def clean(self, row_id=None):
        date_str_a = self.repository.read_cell(row_id, self.col_id_a)
        date_str_b = self.repository.read_cell(row_id, self.col_id_b)
        try:
            date_a = parser.parse(date_str_a, yearfirst=True)
            date_b = parser.parse(date_str_b, yearfirst=True)

            if date_a > date_b:
                return '起始日期大于截至日期'
        except:
            pass
