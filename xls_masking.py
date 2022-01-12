import hashlib
import re
import random
from abc import abstractmethod
import jieba
from settings import *
from xls_repo import XlsRepo

FILE_SUFFIX = '(已脱敏)'

"""
Excel脱敏
"""


@abstractmethod
class Masker(object):
    """
    脱敏策略
    """

    def process(self, origin):
        raise NotImplementedError


class PhoneMasker(Masker):
    """
    电话脱敏策略
    """

    def process(self, origin):
        if len(origin) > 4:
            return origin[0:2] + '*' * (len(origin) - 4) + origin[-2:len(origin)]
        else:
            return origin


class NameMasker(Masker):
    """
    人名脱敏策略
    """

    def process(self, origin):
        pat = re.compile(r'(\w{1})(.*)')
        return pat.sub(r'\1**', origin)


class MoneyMasker(Masker):
    """
    金额脱敏策略
    """

    def process(self, origin):
        return random.randint(0, 99999)


class hash_masker(Masker):
    """
    哈希脱敏策略(相同的值可对应)
    """

    def process(self, origin):
        if len(origin) > 4:
            pat = re.compile(r'(\w{2})(.+)(\w{2})')
            hash = get_hash(origin)
            return pat.sub(r'\1**\3', origin) + hash
        else:
            return origin


class SegMasker(Masker):
    """
    分词脱敏策略(增强可读性)
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


class SegHashMasker(SegMasker):
    """
    分词加哈希脱敏策略
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


def do_masking(method, origin_value):
    """
    数据脱敏
    """
    masker_dict = {
        'PHONE': PhoneMasker(),
        'NAME': NameMasker(),
        'MONEY': MoneyMasker(),
        'HASH': hash_masker(),
        'SEG': SegMasker(),
        'SEGHASH': SegHashMasker(),
    }

    if method not in masker_dict:
        raise RuntimeError('脱敏策略不存在')

    # 获取混淆策略
    masker = masker_dict[method]

    # 生成混淆值
    return masker.process(origin_value)


def process(path, rules):
    """
    Excel脱敏
    :param path: 原始Excel路径
    :param rules: 脱敏规则
    :return: None
    """
    # 打开Excel
    repo = XlsRepo(path)

    # 遍历脱敏规则
    for title_name, method in rules.items():
        col_id = repo.get_col_by_title(title_name)
        print(f'标题名: {title_name}  列: {col_id}  脱敏规则: {method}')

        # 遍历Sheet页
        for row_id in range(repo.title_row_id + 1, repo.row_count):
            # 读取原始值
            origin_value = repo.read_cell(row_id, col_id)
            if origin_value:
                # 生成混淆值
                masking_value = do_masking(method, origin_value)
                # 写入Cell
                repo.write_cell(row_id, col_id, masking_value)

    # 保存Excel
    repo.save_by_suffix(FILE_SUFFIX)


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/项目导入20220110103906.xls'
    rules = {
        '*项目名称': 'SEG',
        '*项目金额': 'MONEY',
    }
    process(path, rules)
