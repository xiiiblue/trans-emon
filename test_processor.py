import unittest

from processor_common import UuidStripProcessor
from processor_masking import SegMaskingProcessor, SegHashMaskingProcessor, HashMaskingProcessor, MoneyMaskingProcessor, \
    NameMaskingProcessor, PhoneMaskingProcessor


class TestProcessor(unittest.TestCase):
    def test_seg_masking(self):
        masker = SegMaskingProcessor()
        src_value = '山东省海内外高层次人才服务专家基地信息化平台'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_seghash_masking(self):
        masker = SegHashMaskingProcessor()
        src_value = '山东省海内外高层次人才服务专家基地信息化平台'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_hash_masking(self):
        masker = HashMaskingProcessor()
        # src_value = '阿里云计算有限公司'
        src_value = '北京市朝阳区北沙滩甲 4 号'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_money_masking(self):
        masker = MoneyMaskingProcessor()
        src_value = 999
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_name_masking(self):
        masker = NameMaskingProcessor()
        src_value = '张三丰'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_phone_masking(self):
        masker = PhoneMaskingProcessor()
        src_value = '053112341234'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_uuid_strip(self):
        masker = UuidStripProcessor(24)
        src_value = '70589931-1F76-4A82-91EA-07976825A349'
        mask_value = masker.process(src_value)
        print(mask_value)
