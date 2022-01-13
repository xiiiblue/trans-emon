from processor_common import TimeFormatProcessor, FillBlankProcessor, FillAllProcessor, DictProcessor, UuidGenerateProcessor, \
    UuidStripProcessor
from processor_masking import PhoneMaskingProcessor, NameMaskingProcessor, HashMaskingProcessor, SegMaskingProcessor, \
    SegHashMaskingProcessor, MoneyMaskingProcessor
from processor_similarity import SimilarityProcessor

# 标题行号
TITLE_ROW = 1

# 有效SHEET页
SHEET_IDX = 0

# 输出文件后缀
FILE_SUFFIX = '(已加工)'

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
    'DICT': DictProcessor,  # 字典替换
    'UUID_GENERATE': UuidGenerateProcessor,  # UUID生成
    'UUID_STRIP': UuidStripProcessor,  # UUID截取
}

# 客户字典
CUST_DICT = {
    '普通客户': '系统内',
    '潜力客户': '系统内',
    '亲密客户': '系统内',
    'TOP客户': '系统内',
    'default': '系统外',
}
