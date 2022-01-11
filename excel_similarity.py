import xlrd
from xlutils.copy import copy

TITLE_ROW = 1
SHEET_IDX = 0
FILE_SUFFIX = '(含相似度建议)'


def get_dest_path(src):
    """
    获取输出文件名
    """
    return f'{src[0:-4]}{FILE_SUFFIX}.xls'


def get_title_col_id(title_name, titles):
    """
    根据标题名获取列ID
    """
    for col_id, title in enumerate(titles):
        if title_name == title:
            return col_id


def similarity(path, src_title, dest_title):
    """
    Excel相似度比对
    :param path: 原始Excel路径
    :return: None
    """
    print(f'输入: {path}')

    # 打开Excel文件
    read_book = xlrd.open_workbook(path, formatting_info=True)
    write_book = copy(read_book)

    # 打开Sheet页
    read_sheet = read_book.sheet_by_index(SHEET_IDX)
    write_sheet = write_book.get_sheet(SHEET_IDX)

    # 获取标题行
    titles = read_sheet.row_values(TITLE_ROW)

    # 获取列ID
    src_col_id = get_title_col_id(src_title, titles)
    dest_col_id = get_title_col_id(dest_title, titles)

    # 遍历Sheet页
    sentence_list = []
    nrows = read_sheet.nrows
    for row_id in range(nrows):
        # 标题及之上的行不处理
        if row_id <= TITLE_ROW:
            continue

        # 读取行
        row = read_sheet.row_values(row_id)

        # 加入列表
        cell_value = row[src_col_id]
        sentence_list.add(cell_value)

    print(sentence_list)

    # 保存Excel
    dest_path = get_dest_path(path)
    write_book.save(dest_path)
    print(f'输出: {dest_path}')


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/客户管理20220110103625.xls'
    src_title = '*项目名称'
    dest_title = '相似项目名称'
    similarity(path, src_title, dest_title)
