from transemon.cleaner import RowCleaner
from transemon.pipeline import Pipeline
from transemon.repository.excel import ExcelRepository

"""
Excel处理流水线
"""


class ExcelPipeline(Pipeline):
    def __init__(self, path, rules):
        self.path = path
        self.rules = rules
        self.repository = ExcelRepository(path)

    def process(self):
        # 遍历规则
        for index, (col_name, method, *args) in enumerate(self.rules):
            # 获取原始列ID及目标列ID
            origin_col_name = col_name.split('|')[0]
            target_col_name = col_name.split('|')[1] if len(col_name.split('|')) > 1 else origin_col_name

            origin_col_id = self.repository.get_col_by_title(origin_col_name)
            target_col_id = self.repository.get_col_by_title(target_col_name)

            # 初始化数据处理器
            cleaner = self.get_cleaner(method, *args)
            method_name = self.get_method_name(method)

            if isinstance(cleaner, RowCleaner):
                cleaner.load(origin_col_id, self.repository)

            print(f'步骤: {index + 1}  标题: {origin_col_name}  规则: {method_name}  参数: {args}')

            # 遍历Sheet页
            for row_id in range(self.repository.title_row_id + 1, self.repository.row_count):

                if isinstance(cleaner, RowCleaner):
                    # 根据行ID清洗数据
                    masking_value = cleaner.clean(row_id)
                else:
                    # 根据原始值清洗数据
                    origin_value = self.repository.read_cell(row_id, origin_col_id)
                    masking_value = cleaner.clean(origin_value)

                # 写入单元格
                if masking_value:
                    self.repository.write_cell(row_id, target_col_id, masking_value)

        # 保存Excel
        self.repository.save()


if __name__ == '__main__':
    path = '/Users/bluexiii/Downloads/export/收入合同20220110103820.xls'
    rules = [
        ('日期比较', None, 'MARK_DATE_COMPARE', '*合同开始日期', '*合同结束日期'),
    ]
    pipeline = ExcelPipeline(path, rules)
    pipeline.process()
