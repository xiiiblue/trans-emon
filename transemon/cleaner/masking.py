import random
import re
from transemon import utils
from transemon.cleaner import CellCleaner

"""
数据脱敏
"""


class PhoneMaskingCleaner(CellCleaner):
    """
    电话脱敏
    """

    def clean(self, origin):
        if len(origin) > 4:
            return origin[0:2] + '*' * (len(origin) - 4) + origin[-2:len(origin)]
        else:
            return origin


class NameMaskingCleaner(CellCleaner):
    """
    人名脱敏
    """

    def clean(self, origin):
        pat = re.compile(r'(\w{1})(.*)')
        return pat.sub(r'\1**', origin)


class MoneyMaskingCleaner(CellCleaner):
    """
    金额脱敏
    """

    def clean(self, origin):
        return random.randint(0, 99999)


class HashMaskingCleaner(CellCleaner):
    """
    哈希脱敏(相同的值可对应)
    """

    def clean(self, origin=None):
        if len(origin) > 4:
            pat = re.compile(r'(\w{2})(.+)(\w{2})')
            hash = utils.md5_hash(origin)
            return pat.sub(r'\1**\3', origin) + hash
        else:
            return origin


class HashAllMaskingCleaner(CellCleaner):
    """
    MD5全哈希脱敏(相同的值可对应)
    """

    def clean(self, origin=None):
        return utils.md5_hash(origin)

class Sha3AllMaskingCleaner(CellCleaner):
    """
    SHA3全哈希脱敏(相同的值可对应)
    """

    def clean(self, origin=None):
        return utils.md5_hash(origin,9999)


class SegMaskingCleaner(CellCleaner):
    """
    分词脱敏(增强可读性)
    """

    def clean(self, origin):
        seg_list = utils.word_segment(origin)
        seg_len = len(seg_list)

        if seg_len < 3:
            plain_positions = [0]
        elif seg_len < 6:
            plain_positions = [0, seg_len - 1]
        elif seg_len < 9:
            plain_positions = [0, int(seg_len / 2), seg_len - 1]
        else:
            plain_positions = [0, int(seg_len / 3), int(seg_len * 2 / 3), seg_len - 1]

        mask_value = ''
        for idx, word in enumerate(seg_list):
            if idx in plain_positions:
                mask_value += word
            else:
                mask_value += '*' * len(word)
        return mask_value


class SegHashMaskingCleaner(SegMaskingCleaner):
    """
    分词加哈希脱敏
    """

    def clean(self, origin):
        seg_value = super().clean(origin)
        hash_value = utils.md5_hash(origin, 8)
        return seg_value + hash_value
