from repository import Repository
from settings import CLEANER

"""
Excel处理流水线
"""


class Pipeline(object):
    def __init__(self, path, rules):
        self.path = path
        self.rules = rules
        self.repository = Repository(path)

    def process(self):
        # 遍历规则
        for index, (col_name, target_col_name, method, *args) in enumerate(self.rules):
            # 获取原始列ID及目标列ID
            origin_col_id = self.repository.get_col_by_title(col_name)
            target_col_id = self.repository.get_col_by_title(target_col_name) if target_col_name else origin_col_id

            # 初始化数据处理器
            cleaner = self.get_cleaner(method, *args)
            method_name = self.get_method_name(method)

            if hasattr(cleaner, 'load'):
                cleaner.load(origin_col_id, self.repository)

            print(f'步骤: {index + 1}  标题: {col_name}  规则: {method_name}  参数: {args}')

            # 遍历Sheet页
            for row_id in range(self.repository.title_row_id + 1, self.repository.row_count):

                if hasattr(cleaner, 'clean_by_id'):
                    # 根据行ID加工数据
                    masking_value = cleaner.clean_by_id(row_id)
                else:
                    # 根据原始值加工数据
                    origin_value = self.repository.read_cell(row_id, origin_col_id)
                    masking_value = cleaner.clean(origin_value)

                # 写入单元格
                if masking_value:
                    self.repository.write_cell(row_id, target_col_id, masking_value)

        # 保存Excel
        self.repository.save()

    @staticmethod
    def get_cleaner(method, *args):
        """
        获取清洗器实例
        """
        if method not in CLEANER:
            raise RuntimeError('数据清洗器不存在')

        return CLEANER[method][0](*args)

    @staticmethod
    def get_method_name(method):
        """
        获取清洗规则名称
        """
        if method not in CLEANER:
            raise RuntimeError('数据清洗器不存在')

        return CLEANER[method][1]


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
