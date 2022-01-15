import json
import os
from pathlib import Path

import fire

from pipeline.excel import ExcelPipeline


def cli(file, config):
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


if __name__ == '__main__':
    fire.Fire(cli)
