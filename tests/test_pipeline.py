import unittest
from pipeline.excel import ExcelPipeline
from settings import PROJECT_SOURCE, CUST_TYPE, PROJECT_TYPE, CONTRACT_TYPE, PAY_TYPE

base_path = '/Users/bluexiii/Downloads/export/'


class TestPipeline(unittest.TestCase):

    def test_pipeline_0(self):
        """
        相似度推荐
        """
        path = f'{base_path}项目导入20220110103906.xls'
        rules = [
            ('项目名称', '相似项目名称', 'MARK_SIMILARITY', 0.9),
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_1(self):
        """
        客户管理
        """
        path = f'{base_path}客户管理20220110103625.xls'
        rules = [
            ('*客户编号', None, 'STRIP_UUID',),
            ('*客户名称', None, 'MASK_SEG_HASH',),
            ('*客户简称', None, 'MASK_SEG_HASH',),
            ('*客户类型', None, 'DICT_REPLACE', CUST_TYPE),
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
        path = f'{base_path}项目导入20220110103906.xls'
        rules = [
            ('*项目编号', None, 'STRIP_UUID',),
            ('*项目名称', None, 'MASK_SEG_HASH',),
            ('*项目类型', None, 'DICT_REPLACE', PROJECT_TYPE),
            ('*项目来源', None, 'DICT_REPLACE', PROJECT_SOURCE),
            ('*立项申请人', None, 'FILL_BLANK', '张三'),
            ('*市场负责人', None, 'FILL_BLANK', '张三'),
            ('*所属部门', None, 'FILL_BLANK', '亿云'),
            ('*项目金额', None, 'MASK_MONEY',),
            ('*立项时间', None, 'FORMAT_TIME',),
            ('*计划验收时间', None, 'FILL_ALL', '2000-01-01'),
            ('*计划结项日期', None, 'FORMAT_TIME',),
            ('*计划结项日期', None, 'FILL_BLANK', '2099-12-31'),
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_3(self):
        """
        供应商
        """
        path = f'{base_path}供应商new.xls'
        rules = [
            ('*供应商编号', None, 'GEN_UUID',),
            ('*供应商名称', None, 'MASK_SEG_HASH',),
            ('*供应商简称', None, 'MASK_SEG_HASH',),
            ('*供应商类型', None, 'FILL_ALL', '系统内'),
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_4(self):
        """
        收入合同
        """
        path = f'{base_path}收入合同20220110103820.xls'
        rules = [
            ('*收入合同编号', None, 'STRIP_UUID',),
            ('*合同名称', None, 'MOCK_SENTENCE',),
            ('*合同甲方', None, 'FILL_ALL', '泰安**新区6378d69bcc4d1e6b'),
            ('*甲方联系人', None, 'MOCK_NAME',),
            ('联系电话', None, 'MOCK_PHONE',),
            ('*合同乙方', None, 'FILL_ALL', '山东亿云信息'),
            ('*合同类型', None, 'DICT_REPLACE', CONTRACT_TYPE),
            ('*支付方式', None, 'DICT_REPLACE', PAY_TYPE),
            ('*市场负责人', None, 'FILL_ALL', 'zhangm'),
            ('*销售部门', None, 'FILL_ALL', '云服务事业部'),
            ('*申请人', None, 'FILL_ALL', 'zhangm'),
            ('*项目编号', None, 'FILL_ALL', '3000000590'),
            ('*合同税率', None, 'FILL_BLANK', '10%'),
            ('*合同金额（元）', None, 'MASK_MONEY',),
            ('*合同开始日期', None, 'FILL_BLANK', '2000-01-01'),
            ('*合同结束日期', None, 'FILL_BLANK', '2050-12-31'),
            ('日期比较', None, 'MARK_DATE_COMPARE', '*合同开始日期', '*合同结束日期'),
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()
