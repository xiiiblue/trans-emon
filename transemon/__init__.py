import json
import os
import fire
from transemon.pipeline.excel import ExcelPipeline
from transemon.settings import set_settings


def commandline(file, config, sheet_idx=0, title_row=1, file_suffix='(已清洗)'):
    """
    Excel数据清洗

    示例:
    transemon 客户管理20220110103625.xls config/cust.json
    transemon --file=客户管理20220110103625.xls --config=config/cust.json
    transemon --file=客户管理20220110103625.xls --config=config/cust.json --sheet_idx=0 --title_row=1 --file_suffix=(已清洗)

    :param file: Excel原始路径
    :param config: 流水线配置JSON路径
    :param sheet_idx: Sheet页码(从0开始)
    :param title_row: 标题行ID(从0开始)
    :param file_suffix: 输出文件后缀
    """
    # 保存全局参数
    if sheet_idx:
        set_settings('TE_SHEET_IDX', str(sheet_idx))
    if title_row:
        set_settings('TE_TITLE_ROW', str(title_row))
    if title_row:
        set_settings('TE_FILE_SUFFIX', str(file_suffix))

    # 转绝对路径
    abs_file_path = os.path.abspath(file)
    abs_config_path = os.path.abspath(config)

    # 解析JSON配置
    json_file = open(abs_config_path)
    rules = json.load(json_file)

    # 流水线处理
    pipeline = ExcelPipeline(abs_file_path, rules)
    pipeline.process()


def bootstrap():
    fire.Fire(commandline)


if __name__ == '__main__':
    bootstrap()
