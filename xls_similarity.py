import jieba

from settings import THRESHOLD
from xls_repo import XlsRepo

FILE_SUFFIX = '(含相似度建议)'

"""
Excel相似度建议
"""


def is_symbol(char):
    """
    判断是否为特殊字符
    """
    symbols = "~!@#$%^&*()_+-*/<>,.[]\/（）【】，。《》"
    for symbol in symbols:
        if char == symbol:
            return True
    return False


def oc_similarity(list_a, list_b):
    """
    判断相似度(Overlap Coefficient算法)
    """
    set_a = set(list_a)
    set_b = set(list_b)
    set_c = set_a.intersection(set_b)
    return float(len(set_c)) / float(min(len(set_a), len(set_b)))


def do_similarity(sentence_dict):
    """
    比较相似度
    """
    # 相似度推荐字典
    similarity_dict = {}

    # 比较相似度
    for src_row_id, (src_sentenct, src_seg_list) in sentence_dict.items():
        similarity_list = []  # 相似行内容数组
        for dest_row_id, (dest_sentenct, dest_seg_list) in sentence_dict.items():
            if src_row_id == dest_row_id:
                continue

            ratio = oc_similarity(src_seg_list, dest_seg_list)
            if ratio > THRESHOLD:
                similarity_list.append((ratio, dest_row_id, dest_sentenct))

        # 加入相似度推荐字典
        if similarity_list:
            similarity_text = similarity_list_to_string(similarity_list)
            similarity_dict[src_row_id] = similarity_text

    return similarity_dict


def similarity_list_to_string(similarity_list):
    """
    相似列表转文本
    """
    text = ''
    for row in similarity_list:
        ratio, dest_row_id, dest_sentence = row
        if text:
            text += '  |  '
        text += f'{dest_sentence}  相似度:{ratio}  行号:{dest_row_id + 1}'
    return text


def process(path, src_title, dest_title):
    """
    Excel相似度建议
    """

    # 打开Excel
    repo = XlsRepo(path)

    # 获取列ID
    src_col_id = repo.get_col_by_title(src_title)
    dest_col_id = repo.get_col_by_title(dest_title)
    print(f'原始标题: {src_title}  原始列ID: {src_col_id}  推荐标题: {dest_title}  推荐列ID: {dest_col_id}')

    # 遍历Sheet页取原始列
    sentence_dict = {}  # 分词字典 行号:(原始句子,分词数组)
    for row_id in range(repo.title_row_id + 1, repo.row_count):
        # 读取单元格
        cell_value = repo.read_cell(row_id, src_col_id)

        # 分词
        seg_list = jieba.lcut(cell_value.strip())

        # 剔除特殊字符
        for seg in seg_list:
            if is_symbol(seg):
                seg_list.remove(seg)

        # 加入分词字典
        sentence_dict[row_id] = (cell_value, seg_list)

    # 比较相似度
    similarity_dict = do_similarity(sentence_dict)

    # 改写Excel
    for row_id in range(repo.title_row_id + 1, repo.row_count):
        # 读取原始单元格
        cell_value = repo.read_cell(row_id, src_col_id)

        if row_id in similarity_dict:
            similarity_text = similarity_dict[row_id]
            repo.write_cell(row_id, dest_col_id, similarity_text)
            print(f'行号: {row_id}  内容: {cell_value}  推荐: {similarity_text}')

    # 保存Excel
    repo.save_by_suffix(FILE_SUFFIX)


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/客户管理20220110103625.xls'
    src_title = '*客户名称'
    dest_title = '相似客户名称推荐'
    process(path, src_title, dest_title)
