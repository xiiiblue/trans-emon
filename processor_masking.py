import hashlib
import random
import re
import jieba
from processor import Processor


class PhoneMaskingProcessor(Processor):
    """
    电话脱敏策略
    """

    def process(self, origin):
        if len(origin) > 4:
            return origin[0:2] + '*' * (len(origin) - 4) + origin[-2:len(origin)]
        else:
            return origin


class NameMaskingProcessor(Processor):
    """
    人名脱敏策略
    """

    def process(self, origin):
        pat = re.compile(r'(\w{1})(.*)')
        return pat.sub(r'\1**', origin)


class MoneyMaskingProcessor(Processor):
    """
    金额脱敏策略
    """

    def process(self, origin):
        return random.randint(0, 99999)


class HashMaskingProcessor(Processor):
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


class SegMaskingProcessor(Processor):
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


class SegHashMaskingProcessor(Processor):
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
