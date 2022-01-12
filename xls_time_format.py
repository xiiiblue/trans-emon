from xlutils.copy import copy
import xlrd

from xls_repo import XlsRepo

FILE_SUFFIX = '(已转换日期)'

"""
Excel时间格式化
"""


def process(path, titles):
    """
    Excel时间格式化
    """
    print(f'输入: {path}')

    # 打开Excel
    repo = XlsRepo(path)

    for title in titles:
        col_id = repo.get_col_by_title(title)

        # 遍历Sheet页
        for row_id in range(repo.title_row_id + 1, repo.row_count):
            # 读取原始值
            origin_value = repo.read_cell(row_id, col_id)

            if origin_value:
                target_value = origin_value[0:10]

                # 写入Cell
                repo.write_cell(row_id, col_id, target_value)

    # 保存Excel
    repo.save_by_suffix(FILE_SUFFIX)


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/项目导入20220110103906(已脱敏).xls'
    titles = ['*计划结项日期', '*立项时间']
    process(path, titles)
