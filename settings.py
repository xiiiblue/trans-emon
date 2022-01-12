# 全局默认配置
from processor_common import TimeFormatProcessor
from processor_masking import PhoneMaskingProcessor, NameMaskingProcessor, HashMaskingProcessor, SegMaskingProcessor, \
    SegHashMaskingProcessor, MoneyMaskingProcessor
from processor_similarity import SimilarityProcessor

TITLE_ROW = 1  # 标题行号
SHEET_IDX = 0  # 有效SHEET页
FILE_SUFFIX = '(已加工)'  # 输出文件后缀

# 数据处理器
PROCESSORS = {
    'PHONE': PhoneMaskingProcessor,  # 电话脱敏
    'NAME': NameMaskingProcessor,  # 人名脱敏
    'MONEY': MoneyMaskingProcessor,  # 金额脱敏
    'HASH': HashMaskingProcessor,  # 哈希脱敏
    'SEG': SegMaskingProcessor,  # 分词脱敏
    'SEGHASH': SegHashMaskingProcessor,  # 分词加哈希脱敏
    'TIME': TimeFormatProcessor,  # 时间格式化
    'SIMILARITY': SimilarityProcessor,  # 相似推荐
}
