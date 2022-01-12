# 全局默认配置
from processor_common import TimeFormatProcessor, FillBlankProcessor, FillAllProcessor, DictProcessor
from processor_masking import PhoneMaskingProcessor, NameMaskingProcessor, HashMaskingProcessor, SegMaskingProcessor, \
    SegHashMaskingProcessor, MoneyMaskingProcessor
from processor_similarity import SimilarityProcessor

TITLE_ROW = 1  # 标题行号
SHEET_IDX = 0  # 有效SHEET页
FILE_SUFFIX = '(已加工)'  # 输出文件后缀

# 数据处理器
PROCESSORS = {
    'MASK_PHONE': PhoneMaskingProcessor,  # 电话脱敏
    'MASK_NAME': NameMaskingProcessor,  # 人名脱敏
    'MASK_MONEY': MoneyMaskingProcessor,  # 金额脱敏
    'MASK_HASH': HashMaskingProcessor,  # 哈希脱敏
    'MASK_SEG': SegMaskingProcessor,  # 分词脱敏
    'MASK_SEG_HASH': SegHashMaskingProcessor,  # 分词加哈希脱敏
    'FORMAT_TIME': TimeFormatProcessor,  # 时间格式化
    'SIMILARITY': SimilarityProcessor,  # 相似推荐
    'FILL_BLANK': FillBlankProcessor,  # 空白填充
    'FILL_ALL': FillAllProcessor,  # 全量填充
    'REPLACE_DICT': DictProcessor,  # 字典替换
}
