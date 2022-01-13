from cleaner.common import TimeFormatCleaner, FillBlankCleaner, FillAllCleaner, DictReplaceCleaner, UuidGenerateCleaner, UuidStripCleaner
from cleaner.masking import NameMaskingCleaner, HashMaskingCleaner, SegMaskingCleaner, SegHashMaskingCleaner, MoneyMaskingCleaner, \
    PhoneMaskingCleaner
from cleaner.similarity import SimilarityCleaner

TITLE_ROW = 1

# 有效SHEET页
SHEET_IDX = 0

# 输出文件后缀
FILE_SUFFIX = '(已加工)'

# 数据清洗器
CLEANER = {
    'MASK_PHONE': (PhoneMaskingCleaner, '电话脱敏'),
    'MASK_NAME': (NameMaskingCleaner, '姓名脱敏'),
    'MASK_MONEY': (MoneyMaskingCleaner, '金额脱敏'),
    'MASK_HASH': (HashMaskingCleaner, '哈希脱敏'),
    'MASK_SEG': (SegMaskingCleaner, '分词脱敏'),
    'MASK_SEG_HASH': (SegHashMaskingCleaner, '分词加哈希脱敏'),
    'FORMAT_TIME': (TimeFormatCleaner, '时间格式化'),
    'SIMILARITY': (SimilarityCleaner, '相似推荐'),
    'FILL_BLANK': (FillBlankCleaner, '空白填充'),
    'FILL_ALL': (FillAllCleaner, '全量填充'),
    'DICT': (DictReplaceCleaner, '字典替换'),
    'UUID_GENERATE': (UuidGenerateCleaner, 'UUID生成'),
    'UUID_STRIP': (UuidStripCleaner, 'UUID截取'),
}

# 客户字典
CUST_DICT = {
    '普通客户': '系统内',
    '潜力客户': '系统内',
    '亲密客户': '系统内',
    'TOP客户': '系统内',
    'default': '系统外',
}
