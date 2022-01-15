import json
import os
import fire

from transemon.pipeline.excel import ExcelPipeline


def cli(file, config):
    """
    Excel数据清晰

    示例:
    python transemon.py --file=/Users/bluexiii/Downloads/export/客户管理20220110103625.xls --config=config/cust.json

    :param file: Excel原始路径
    :param config: 流水线配置JSON路径
    """

    # 转绝对路径
    abs_file_path = os.path.abspath(file)
    abs_config_path = os.path.abspath(config)
    print("abs_file_path =", abs_file_path)
    print("abs_config_path =", abs_config_path)

    # 解析JSON配置
    json_file = open(abs_config_path)
    rules = json.load(json_file)

    # 流水线处理
    pipeline = ExcelPipeline(abs_file_path, rules)
    pipeline.process()


def entry():
    fire.Fire(cli)


if __name__ == '__main__':
    entry()
