from repository import Repository
from settings import PROCESSORS

"""
Excel处理流水线
"""


class Pipeline(object):
    def __init__(self, path, rules):
        self.path = path
        self.rules = rules
        # 初始化Excel仓库
        self.repo = Repository(path)

    def get_processor(self, method, *args):
        """
        获取数据处理器实例
        """
        if method not in PROCESSORS:
            raise RuntimeError('数据处理器不存在')

        return PROCESSORS[method](*args)

    def process(self):
        # 遍历规则
        for index, (col_name, target_col_name, method, *args) in enumerate(rules):
            # 获取原始列ID及目标列ID
            origin_col_id = self.repo.get_col_by_title(col_name)
            target_col_id = self.repo.get_col_by_title(target_col_name) if target_col_name else origin_col_id

            # 初始化数据处理器
            processor = self.get_processor(method, *args)
            if hasattr(processor, 'pre_process'):
                processor.pre_process(origin_col_id, self.repo)

            print(f'步骤: {index + 1}  标题: {col_name}  规则: {method}  参数: {args}')

            # 遍历Sheet页
            for row_id in range(self.repo.title_row_id + 1, self.repo.row_count):

                if hasattr(processor, 'process_by_id'):
                    # 根据行ID加工数据
                    masking_value = processor.process_by_id(row_id)
                else:
                    # 根据原始值加工数据
                    origin_value = self.repo.read_cell(row_id, origin_col_id)
                    masking_value = processor.process(origin_value)

                # 写入单元格
                self.repo.write_cell(row_id, target_col_id, masking_value)

        # 保存Excel
        self.repo.save()


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/项目导入20220110103906.xls'
    rules = [
        # ('*项目名称', None, 'SEG', None,(None)),
        ('*项目金额', None, 'MONEY', None),
        ('*立项时间', None, 'TIME', None),
        ('*项目名称', '相似项目名称', 'SIMILARITY', 0.9),
    ]
    pipeline = Pipeline(path, rules)
    pipeline.process()
