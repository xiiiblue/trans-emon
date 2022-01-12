from xlutils.copy import copy
import xlrd

TITLE_ROW = 1
SHEET_IDX = 0
FILE_SUFFIX = '(已转换日期)'


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


def time_to_date(path, titles):
    """
    时间转日期
    :param path: 原始Excel路径
    :param rules: 脱敏规则
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
    all_titles = read_sheet.row_values(TITLE_ROW)

    for title in titles:
        col_id = get_title_col_id(title, all_titles)

        if not col_id:
            raise RuntimeError('根据标题找不到对应的列ID')

        # 遍历Sheet页
        nrows = read_sheet.nrows
        for row_id in range(nrows):
            # 标题及之上的行不处理
            if row_id <= TITLE_ROW:
                continue

            # 读取行
            row = read_sheet.row_values(row_id)

            # 读取原始值
            time_value = row[col_id]

            if time_value:
                date_value = time_value[0:10]
                # 写入Cell
                write_sheet.write(row_id, col_id, date_value)

    # 保存Excel
    dest_path = get_dest_path(path)
    write_book.save(dest_path)
    print(f'输出: {dest_path}')


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/项目导入20220110103906(已脱敏).xls'
    titles = ['*计划结项日期', '*立项时间']
    time_to_date(path, titles)
