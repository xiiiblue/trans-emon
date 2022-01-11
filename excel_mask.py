import hashlib
import re
import random
from abc import abstractmethod

import jieba
from xlutils.copy import copy
import xlrd

TITLE_ROW = 1
SHEET_IDX = 0
FILE_SUFFIX = '(已脱敏)'


@abstractmethod
class masker():
    """
    混淆策略
    """

    def process(self, origin):
        raise NotImplementedError


class phone_masker(masker):
    """
    混淆电话号码
    """

    def process(self, origin):
        if len(origin) > 4:
            return origin[0:2] + '*' * (len(origin) - 4) + origin[-2:len(origin)]
        else:
            return origin


class name_masker(masker):
    """
    混淆人名
    """

    def process(self, origin):
        pat = re.compile(r'(\w{1})(.*)')
        return pat.sub(r'\1**', origin)


class money_masker(masker):
    """
    混淆金额
    """

    def process(self, origin):
        return random.randint(0, 99999)


class hash_masker(masker):
    """
    哈希(相同的值混淆后可一一对应)
    """

    def process(self, origin):
        if len(origin) > 4:
            pat = re.compile(r'(\w{2})(.+)(\w{2})')
            hash = get_hash(origin)
            return pat.sub(r'\1**\3', origin) + hash
        else:
            return origin


class seg_masker(masker):
    """
    分词(对于长文本增强可读性)
    """

    def process(self, origin):
        seg_list = jieba.lcut(origin)
        seg_len = len(seg_list)

        if seg_len < 10:
            plain_positions = [0, seg_len - 1]
        elif seg_len < 20:
            plain_positions = [0, int(seg_len / 2), seg_len - 1]
        elif seg_len < 30:
            plain_positions = [0, int(seg_len / 3), int(seg_len * 2 / 3), seg_len - 1]
        else:
            plain_positions = [0, int(seg_len / 4), int(seg_len * 2 / 4), int(seg_len * 3 / 4), seg_len - 1]

        mask_value = ''
        for idx, word in enumerate(seg_list):
            if idx in plain_positions:
                mask_value += word
            else:
                mask_value += '*' * len(word)
        return mask_value


class seghash_masker(seg_masker):
    """
    分词且哈希
    """

    def process(self, origin):
        seg_value = super().process(origin)
        hash_value = get_hash(origin)
        return seg_value + hash_value


def get_hash(origin):
    """
    获取16位哈希值
    """
    md5 = hashlib.md5()
    md5.update(origin.encode('utf-8'))
    return md5.hexdigest()[8:-8]


def get_masker(method):
    """
    获取混淆策略
    :param method: 策略名称
    :return:
    """
    masker_dict = {
        'PHONE': phone_masker(),
        'NAME': name_masker(),
        'MONEY': money_masker(),
        'HASH': hash_masker(),
        'SEG': seg_masker(),
        'SEGHASH': seghash_masker(),
    }

    if method not in masker_dict:
        raise RuntimeError('脱敏策略不存在')

    return masker_dict[method]


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


def mask(path, rules):
    """
    Excel脱敏
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
    titles = read_sheet.row_values(TITLE_ROW)

    # 遍历脱敏规则
    for title_name, method in rules.items():
        col_id = get_title_col_id(title_name, titles)
        print(f'标题名: {title_name}  列: {col_id}  脱敏规则: {method}')

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
            src_value = row[col_id]
            if src_value:
                # 获取混淆策略
                masker = get_masker(method)

                # 生成混淆值
                mask_value = masker.process(src_value)

                # 写入Cell
                write_sheet.write(row_id, col_id, mask_value)

    # 保存Excel
    dest_path = get_dest_path(path)
    write_book.save(dest_path)
    print(f'输出: {dest_path}')


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/项目导入20220110103906.xls'
    rules = {
        '*项目名称': 'SEG',
        '*项目金额': 'MONEY',
    }
    mask(path, rules)
