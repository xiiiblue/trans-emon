from transemon.cleaner import RowCleaner

"""
标记重复
"""


class DuplicateCleaner(RowCleaner):

    def __init__(self, *args):
        super().__init__(*args)
        self.data_list = []
        self.origin_col_id = 0
        self.repository = None

    def load(self, origin_col_id, repository):
        self.origin_col_id = origin_col_id
        self.repository = repository

        for row_id in range(repository.title_row_id + 1, repository.row_count):
            cell_value = repository.read_cell(row_id, origin_col_id)
            self.data_list.append(cell_value)

    def clean(self, row_id=None):
        origin_value = self.repository.read_cell(row_id, self.origin_col_id)
        return self.data_list.count(origin_value)
