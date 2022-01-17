import unittest

from transemon.cleaner.common import StripUuidCleaner
from transemon.cleaner.masking import SegMaskingCleaner, SegHashMaskingCleaner, HashMaskingCleaner, MoneyMaskingCleaner, \
    NameMaskingCleaner, PhoneMaskingCleaner
from transemon.cleaner.mock import MockNameCleaner


class TestCleaner(unittest.TestCase):
    def test_seg_masking(self):
        masker = SegMaskingCleaner()
        src_value = '山东省海内外高层次人才服务专家基地信息化平台'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_seghash_masking(self):
        masker = SegHashMaskingCleaner()
        src_value = '山东省海内外高层次人才服务专家基地信息化平台'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_hash_masking(self):
        masker = HashMaskingCleaner()
        # src_value = '阿里云计算有限公司'
        src_value = '北京市朝阳区北沙滩甲 4 号'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_money_masking(self):
        masker = MoneyMaskingCleaner()
        src_value = 999
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_name_masking(self):
        masker = NameMaskingCleaner()
        src_value = '张三丰'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_phone_masking(self):
        masker = PhoneMaskingCleaner()
        src_value = '053112341234'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_uuid_strip(self):
        masker = StripUuidCleaner(24)
        src_value = '70589931-1F76-4A82-91EA-07976825A349'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_mock_name(self):
        cleaner = MockNameCleaner()
        target_value = cleaner.clean()
        print(target_value)
