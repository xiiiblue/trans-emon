import unittest
from pipeline.excel import ExcelPipeline
from settings import CUST_DICT


class TestPipeline(unittest.TestCase):

    def test_pipeline_0(self):
        """
        相似度推荐
        """
        path = '/Users/bluexiii/Downloads/export/项目导入20220110103906.xls'
        rules = [
            ('项目名称', '相似项目名称', 'SIMILARITY', 0.9),
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_1(self):
        """
        客户管理
        """
        path = '/Users/bluexiii/Downloads/export/客户管理20220110103625.xls'
        rules = [
            ('*客户编号', None, 'STRIP_UUID',),
            ('*客户名称', None, 'MASK_SEG_HASH',),
            ('*客户简称', None, 'MASK_SEG_HASH',),
            ('*客户类型', None, 'DICT_REPLACE', CUST_DICT),
            ('联系人', None, 'MASK_NAME',),
            ('联系人', None, 'FILL_BLANK', '张三'),
            ('电话', None, 'MOCK_PHONE',),
            ('地址', None, 'MASK_SEG',),
            ('法定代表人', None, 'MOCK_NAME',),
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_2(self):
        """
        项目
        """
        path = '/Users/bluexiii/Downloads/export/项目导入20220110103906.xls'
        rules = [
            ('*项目编号', None, 'STRIP_UUID',),
            ('*项目名称', None, 'MASK_SEG_HASH',),
            ('*项目类型', None, 'DICT_REPLACE', {'软件开发': '系统内', 'default': '系统外'}),
            ('*项目金额', None, 'MASK_MONEY',),
            ('*立项时间', None, 'FORMAT_TIME',),
            ('*计划结项日期', None, 'FORMAT_TIME',),
            ('*计划结项日期', None, 'FILL_BLANK', '2099-12-31'),
            ('*计划验收时间', None, 'FILL_ALL', '2000-01-01'),
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_3(self):
        """
        供应商
        """
        path = '/Users/bluexiii/Downloads/export/供应商new.xls'

        rules = [
            ('*供应商名称', None, 'MASK_HASH', None),
            ('*供应商简称', None, 'MASK_HASH', None),
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()
