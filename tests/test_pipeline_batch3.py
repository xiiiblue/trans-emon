import unittest
from transemon.pipeline.excel import ExcelPipeline

base_path = "/Users/bluexiii/Documents/evayinfo/61金现代OA/20220119历史数据导入/"


class TestPipeline(unittest.TestCase):

    def test_pipeline_04(self):
        """
        04收入合同
        """
        path = f"{base_path}04收入合同V3.xls"
        rules = [
            ["*支付方式", "FILL_ALL", "3:6:1"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_05(self):
        """
        05成本合同
        """
        path = f"{base_path}05成本合同V2.xls"
        rules = [
            ["*支付方式", "FILL_ALL", "0:10"],
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
