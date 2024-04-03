import unittest
from transemon.pipeline.excel import ExcelPipeline

base_path = "/Users/bluexiii/Downloads/"


class TestPipeline(unittest.TestCase):

    def test_pipeline_01(self):
        path = f"{base_path}买药信息.xls"
        rules = [
            ["身份证", "MASK_HASH_ALL"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()
