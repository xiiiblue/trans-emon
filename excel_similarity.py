import jieba
import xlrd
from xlutils.copy import copy

TITLE_ROW = 1
SHEET_IDX = 0
FILE_SUFFIX = '(含相似度建议)'
THRESHOLD = 0.9


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


def is_symbol(char):
    """
    判断是否为特殊字符
    """
    symbols = "~!@#$%^&*()_+-*/<>,.[]\/（）【】，。《》"
    for symbol in symbols:
        if char == symbol:
            return True
    return False


def get_oc_similarity(list_a, list_b):
    """
    判断相似度(Overlap Coefficient算法)
    """
    set_a = set(list_a)
    set_b = set(list_b)
    set_c = set_a.intersection(set_b)
    return float(len(set_c)) / float(min(len(set_a), len(set_b)))


def format_similarity_list(similarity_list):
    """
    格式化相似内容列表
    """
    text = ''
    for row in similarity_list:
        ratio, dest_row_id, dest_sentence = row
        if text:
            text += '  |  '
        text += f'{dest_sentence}  相似度:{ratio}  行号:{dest_row_id}'
    return text


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

    print(f'原始标题: {src_title}  原始列ID: {src_col_id}  推荐标题: {dest_title}  推荐列ID: {dest_col_id}')

    if not src_col_id or not dest_col_id:
        raise RuntimeError('标题名称不存在')

    # 遍历Sheet页取原始列
    sentence_dict = {}
    nrows = read_sheet.nrows
    for row_id in range(nrows):
        # 标题及之上的行不处理
        if row_id <= TITLE_ROW:
            continue

        # 读取行
        row = read_sheet.row_values(row_id)

        # 读取单元格
        cell_value = row[src_col_id]

        # 分词
        seg_list = jieba.lcut(cell_value.strip())

        # 剔除特殊字符
        for seg in seg_list:
            if is_symbol(seg):
                seg_list.remove(seg)

        # 加入字典
        cell_data = (cell_value, seg_list)
        sentence_dict[row_id] = cell_data

    # 比较相似度
    similarity_dict = {}
    for src_row_id, src_cell_data in sentence_dict.items():
        src_sentenct, src_seg_list = src_cell_data
        similarity_list = []
        for dest_row_id, dest_cell_data in sentence_dict.items():
            dest_sentenct, dest_seg_list = dest_cell_data
            if src_row_id == dest_row_id:
                continue
            ratio = get_oc_similarity(src_seg_list, dest_seg_list)
            if ratio > THRESHOLD:
                similarity_list.append((ratio, dest_row_id, dest_sentenct))

        if similarity_list:
            similarity_dict[src_row_id] = similarity_list

    print(similarity_dict)

    # 改写Excel
    for row_id in range(nrows):
        if row_id <= TITLE_ROW:
            continue

        # 读取行
        row = read_sheet.row_values(row_id)

        # 读取单元格
        cell_value = row[src_col_id]

        if row_id in similarity_dict:
            similarity_list = similarity_dict[row_id]
            similarity_text = format_similarity_list(similarity_list)
            print(f'行号: {row_id}  内容: {cell_value}  推荐: {similarity_text} \n')
            write_sheet.write(row_id, dest_col_id, similarity_text)

    # 保存Excel
    dest_path = get_dest_path(path)
    write_book.save(dest_path)
    print(f'输出: {dest_path}')


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/客户管理20220110103625.xls'
    src_title = '*客户名称'
    dest_title = '相似客户名称推荐'
    similarity(path, src_title, dest_title)
