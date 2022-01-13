import hashlib

import jieba


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


def md5_hash(origin, length=16):
    """
    获取哈希值
    """
    md5 = hashlib.md5()
    md5.update(origin.encode('utf-8'))
    return md5.hexdigest()[0:length]


def word_segment(sentence):
    """
    分词
    """
    # 分词
    seg_list = jieba.lcut(sentence.strip())

    # 剔除特殊字符
    for seg in seg_list:
        if is_symbol(seg):
            seg_list.remove(seg)

    return seg_list
