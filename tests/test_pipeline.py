import unittest
from transemon.pipeline.excel import ExcelPipeline
from config.dicts import PROJECT_SOURCE, CUST_TYPE, PROJECT_TYPE, PAY_TYPE, CHECK_LIST, INCOME_CONTRACT_TYPE, SETTLE_TYPE

base_path = "/Users/bluexiii/Downloads/export/"


class TestPipeline(unittest.TestCase):

    def test_pipeline_0(self):
        """
        相似度推荐
        """
        path = f"{base_path}项目导入20220110103906.xls"
        rules = [
            ["项目名称|相似项目名称", "MARK_SIMILARITY", 0.9],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_1(self):
        """
        客户管理
        """
        path = f"{base_path}客户管理20220110103625.xls"
        rules = [
            ["*客户编号", "STRIP_UUID"],
            ["*客户名称", "MASK_SEG_HASH"],
            ["*客户简称", "MASK_SEG_HASH"],
            ["*客户类型", "DICT_REPLACE", CUST_TYPE],
            ["联系人", "MASK_NAME"],
            ["联系人", "FILL_BLANK", "张三"],
            ["电话", "MOCK_PHONE"],
            ["地址", "MASK_SEG"],
            ["法定代表人", "MOCK_NAME"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_2(self):
        """
        项目
        """
        path = f"{base_path}项目导入20220110103906.xls"
        rules = [
            ["*项目编号", "STRIP_UUID"],
            ["*项目名称", "MASK_SEG_HASH"],
            ["*项目类型", "DICT_REPLACE", PROJECT_TYPE],
            ["*项目来源", "DICT_REPLACE", PROJECT_SOURCE],
            ["*立项申请人", "FILL_BLANK", "张三"],
            ["*市场负责人", "FILL_BLANK", "张三"],
            ["*所属部门", "FILL_BLANK", "亿云"],
            ["*项目金额", "MASK_MONEY"],
            ["*立项时间", "FORMAT_TIME"],
            ["*计划验收时间", "FILL_ALL", "2000-01-01"],
            ["*计划结项日期", "FORMAT_TIME"],
            ["*计划结项日期", "FILL_BLANK", "2099-12-31"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_3(self):
        """
        供应商
        """
        path = f"{base_path}供应商new.xls"
        rules = [
            ["*供应商编号", "GEN_UUID"],
            ["*供应商名称", "MASK_SEG_HASH"],
            ["*供应商简称", "MASK_SEG_HASH"],
            ["*供应商类型", "FILL_ALL", "系统内"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_4(self):
        """
        收入合同
        """
        path = f"{base_path}收入合同20220110103820.xls"
        rules = [
            ["*收入合同编号", "STRIP_UUID"],
            ["*合同名称", "MOCK_SENTENCE"],
            ["*合同甲方", "FILL_ALL", "泰安**新区6378d69bcc4d1e6b"],
            ["*甲方联系人", "MOCK_NAME"],
            ["联系电话", "MOCK_PHONE", ],
            ["*合同乙方", "FILL_ALL", "山东亿云信息"],
            ["*合同类型", "DICT_REPLACE", INCOME_CONTRACT_TYPE],
            ["*支付方式", "DICT_REPLACE", PAY_TYPE],
            ["*市场负责人", "FILL_ALL", "zhangm"],
            ["*销售部门", "FILL_ALL", "云服务事业部"],
            ["*申请人", "FILL_ALL", "zhangm"],
            ["*项目编号", "FILL_ALL", "3000000590"],
            ["*合同税率", "FILL_BLANK", "10%"],
            ["*合同金额（元）", "MASK_MONEY"],
            ["*合同开始日期", "FILL_BLANK", "2000-01-01"],
            ["*合同结束日期", "FILL_BLANK", "2050-12-31"],
            ["日期比较|日期比较", "MARK_DATE_COMPARE", "*合同开始日期", "*合同结束日期"],
            ["*合同结束日期|异常清单", "MARK_CHECK_LIST", CHECK_LIST],
            ["*收入合同编号|重复次数", "MARK_DUPLICATE"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_5(self):
        """
        成本合同
        """
        path = f"{base_path}成本合同20220110235959(1).xls"
        rules = [
            ["*合同编号", "STRIP_UUID"],
            ["*合同名称", "MOCK_SENTENCE"],
            ["*合同甲方", "FILL_ALL", "山东亿云信息"],
            ["*合同乙方", "FILL_ALL", "山东**公司61d6d6674a0f0903"],
            ["*乙方联系人", "MOCK_NAME"],
            ["*合同类型", "FILL_ALL", "实施技术外采"],
            ["*支付方式", "DICT_REPLACE", PAY_TYPE],
            ["*申请人", "FILL_ALL", "zhangm"],
            ["*合同负责人", "FILL_ALL", "zhangm"],
            ["*所属部门", "FILL_ALL", "云服务事业部"],
            ["*项目编号", "FILL_ALL", "3000000590"],
            ["*税率", "FILL_BLANK", "10%"],
            ["*合同开始时间", "FILL_BLANK", "2000-01-01"],
            ["*合同结束时间", "FILL_BLANK", "2050-12-31"],
            ["*合同编号|重复次数", "MARK_DUPLICATE"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()

    def test_pipeline_5_2(self):
        """
        回款
        """
        path = f"{base_path}回款测试.xls"
        rules = [
            ["*回款编号", "STRIP_UUID"],
            ["*回款单位", "FILL_ALL", "泰安**新区6378d69bcc4d1e6b"],
            ["*结算方式", "DICT_REPLACE", SETTLE_TYPE],
            ["*认领金额(元)", "MASK_MONEY"],
            ["*收入合同编号", "STRIP_UUID"],
            ["*项目编号", "STRIP_UUID"],
            ["*认领人", "FILL_ALL", "管理员(admin)"],
            ["*收入合同编号", "FILL_ALL", "C752771C58C0480E"],
            ["*项目编号", "FILL_ALL", "3000000590"],
        ]
        pipeline = ExcelPipeline(path, rules)
        pipeline.process()
