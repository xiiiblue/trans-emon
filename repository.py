from xlutils.copy import copy
import xlrd

from settings import SHEET_IDX, TITLE_ROW, FILE_SUFFIX


class Repository(object):
    """
    Excel仓库
    """

    def __init__(self, src_path):
        """
        初始化Excel
        """
        print(f'打开Excel: {src_path}')
        # 原始路径
        self.src_path = src_path

        # 打开Excel文件
        self.read_book = xlrd.open_workbook(src_path, formatting_info=True)
        self.write_book = copy(self.read_book)

        # 打开Sheet页
        self.read_sheet = self.read_book.sheet_by_index(SHEET_IDX)
        self.write_sheet = self.write_book.get_sheet(SHEET_IDX)

        # 总行数
        self.row_count = self.read_sheet.nrows

        # 标题行ID
        self.title_row_id = TITLE_ROW

        # 标题行
        self.titles = self.read_sheet.row_values(self.title_row_id)

    def get_row(self, row_id):
        """
        获取一行
        """
        return self.read_sheet.row_values(row_id)

    def read_cell(self, row_id, col_id):
        """
        获取单元格
        """
        row = self.get_row(row_id)
        return row[col_id]

    def write_cell(self, row_id, col_id, value):
        self.write_sheet.write(row_id, col_id, value)

    def save_by_path(self, dest_path):
        """
        保存Excel(完整路径)
        """
        print(f'保存Excel: {dest_path}')
        self.write_book.save(dest_path)

    def save_by_suffix(self, suffix):
        """
        保存Excel(后缀)
        """
        dest_path = f'{self.src_path[0:-4]}{suffix}.xls'
        self.save_by_path(dest_path)

    def save(self):
        """
        保存Excel
        """
        self.save_by_suffix(FILE_SUFFIX)

    def get_col_by_title(self, title_name):
        """
        根据标题名获取列ID
        """
        for col_id, title in enumerate(self.titles):
            if title_name == title:
                return col_id

        raise RuntimeError('根据标题找不到对应的列ID')
