import unittest

from pipeline import Pipeline


class TestPipeline(unittest.TestCase):

    def test_pipeline_1(self):
        """
        客户管理
        """
        path = '/Users/bluexiii/Downloads/export/客户管理20220110103625.xls'
        rules = [
            ('*客户名称', 'HASH', None),
            ('*客户简称', 'HASH', None),
            ('联系人', 'NAME', None),
            ('电话', 'PHONE', None),
            ('地址', 'HASH', None),
        ]
        pipeline = Pipeline(path, rules)
        pipeline.process()

    def test_pipeline_2(self):
        """
        项目
        """
        path = '/Users/bluexiii/Downloads/export/项目导入20220110103906.xls'
        rules = [
            ('*项目名称', 'SEG', None),
            ('*项目金额', 'MONEY', None),
            ('*立项时间', 'TIME', None),
        ]
        pipeline = Pipeline(path, rules)
        pipeline.process()

    def test_pipeline_3(self):
        """
        供应商
        """
        path = '/Users/bluexiii/Downloads/export/供应商new.xls'

        rules = [
            ('*供应商名称', 'HASH', None),
            ('*供应商简称', 'HASH', None),
        ]
        pipeline = Pipeline(path, rules)
        pipeline.process()
