import unittest

from processor_masking import SegMaskingProcessor, SegHashMaskingProcessor, HashMaskingProcessor, MoneyMaskingProcessor, \
    NameMaskingProcessor, PhoneMaskingProcessor


class TestProcessor(unittest.TestCase):
    def test_seg_masker(self):
        masker = SegMaskingProcessor()
        src_value = '山东省海内外高层次人才服务专家基地信息化平台'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_seghash_masker(self):
        masker = SegHashMaskingProcessor()
        src_value = '山东省海内外高层次人才服务专家基地信息化平台'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_hash_masker(self):
        masker = HashMaskingProcessor()
        # src_value = '阿里云计算有限公司'
        src_value = '北京市朝阳区北沙滩甲 4 号'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_money_masker(self):
        masker = MoneyMaskingProcessor()
        src_value = 999
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_name_masker(self):
        masker = NameMaskingProcessor()
        src_value = '张三丰'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_phone_masker(self):
        masker = PhoneMaskingProcessor()
        src_value = '053112341234'
        mask_value = masker.process(src_value)
        print(mask_value)

    def test_masking_1(self):
        """
        客户管理
        """
        path = '/Users/bluexiii/Downloads/export/客户管理20220110103625.xls'
        rules = {
            '*客户名称': 'HASH',
            '*客户简称': 'HASH',
            '联系人': 'NAME',
            '电话': 'PHONE',
            '地址': 'HASH',
        }
        process(path, rules)

    def test_masking_2(self):
        """
        项目
        """
        path = '/Users/bluexiii/Downloads/export/项目导入20220110103906.xls'
        rules = {
            '*项目名称': 'HASH',
            '*项目金额': 'MONEY',
        }
        process(path, rules)

    def test_masking_3(self):
        """
        供应商
        """
        path = '/Users/bluexiii/Downloads/export/供应商new.xls'
        rules = {
            '*供应商名称': 'HASH',
            '*供应商简称': 'HASH',
        }
        process(path, rules)
