import unittest
from transemon.pipeline.excel import ExcelPipeline

base_path = "/Users/bluexiii/Documents/evayinfo/61金现代OA/20220119历史数据导入/"


class TestPipeline(unittest.TestCase):

    def test_pipeline_01(self):
        """
        01客户基本信息
        """
        path = f"{base_path}01客户基本信息V2.xls"
        rules = [
            ["*客户名称", "MASK_SEG_HASH"],
            ["*客户简称", "MASK_SEG_HASH"],
            ["联系人", "MASK_NAME"],
            ["电话", "MOCK_PHONE"],
            ["地址", "MASK_SEG"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_02(self):
        """
        02供应商
        """
        path = f"{base_path}02供应商V2.xls"
        rules = [
            ["*供应商名称", "MASK_SEG_HASH"],
            ["*供应商简称", "MASK_SEG_HASH"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_03(self):
        """
        03项目基本信息
        """
        path = f"{base_path}03项目基本信息V2.xls"
        rules = [
            ["*项目名称", "MASK_SEG_HASH"],
            ["*项目金额", "MASK_MONEY"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_04(self):
        """
        04收入合同
        """
        path = f"{base_path}04收入合同V3.xls"
        rules = [
            ["*合同甲方", "MASK_SEG_HASH"],
            ["*甲方联系人", "MASK_SEG_HASH"],
            ["*合同金额（元）", "MASK_MONEY"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_04_2(self):
        """
        04收入合同-虚拟客户
        """
        path = f"{base_path}00虚拟客户收入合同.xls"
        rules = [
            ["*客户名称", "MASK_SEG_HASH"],
            ["*客户简称", "MASK_SEG_HASH"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_05(self):
        """
        05成本合同
        """
        path = f"{base_path}05成本合同V2.xls"
        rules = [
            ["*合同名称", "MASK_SEG_HASH"],
            ["*合同乙方", "MASK_SEG_HASH"],
            ["*乙方联系人", "MASK_NAME"],
            ["立项预算金额", "MASK_MONEY"],
            ["*分摊金额（元）", "MASK_MONEY"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_05_2(self):
        """
        05成本合同-虚拟供应商
        """
        path = f"{base_path}05成本合同@虚拟供应商.xls"
        rules = [
            ["*供应商名称", "MASK_SEG_HASH"],
            ["*供应商简称", "MASK_SEG_HASH"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_07(self):
        """
        07费用报销
        """
        path = f"{base_path}07费用报销V3.xls"
        rules = [
            ["*费用编号", "STRIP_UUID"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_08(self):
        """
        08差旅报销
        """
        path = f"{base_path}08差旅报销V2.xls"
        rules = [
            ["*差旅编号", "STRIP_UUID"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()
