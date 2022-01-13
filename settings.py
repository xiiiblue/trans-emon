from cleaner.common import TimeFormatCleaner, FillBlankCleaner, FillAllCleaner, DictReplaceCleaner, StripUuidCleaner, StripStringCleaner
from cleaner.compare import DateCompareCleaner
from cleaner.generater import GenerateUuidCleaner, GenerateRandomNumberCleaner, GenerateSequenceCleaner
from cleaner.masking import NameMaskingCleaner, HashMaskingCleaner, SegMaskingCleaner, SegHashMaskingCleaner, MoneyMaskingCleaner, \
    PhoneMaskingCleaner
from cleaner.mock import MockAddressCleaner, MockCityCleaner, MockZipCodeCleaner, MockNameCleaner, MockCompanyCleaner, MockPhoneCleaner, \
    MockSentenceCleaner
from cleaner.similarity import SimilarityCleaner

TITLE_ROW = 1

# 有效SHEET页
SHEET_IDX = 0

# 输出文件后缀
FILE_SUFFIX = '(已清洗)'

# 数据清洗器
CLEANER = {
    'MASK_PHONE': (PhoneMaskingCleaner, '电话脱敏'),
    'MASK_NAME': (NameMaskingCleaner, '姓名脱敏'),
    'MASK_MONEY': (MoneyMaskingCleaner, '金额脱敏'),
    'MASK_HASH': (HashMaskingCleaner, '哈希脱敏'),
    'MASK_SEG': (SegMaskingCleaner, '分词脱敏'),
    'MASK_SEG_HASH': (SegHashMaskingCleaner, '分词加哈希脱敏'),
    'FORMAT_TIME': (TimeFormatCleaner, '时间格式化'),
    'FILL_BLANK': (FillBlankCleaner, '空白填充'),
    'FILL_ALL': (FillAllCleaner, '全量填充'),
    'DICT_REPLACE': (DictReplaceCleaner, '字典替换'),
    'GEN_UUID': (GenerateUuidCleaner, '生成UUID'),
    'GEN_NUM': (GenerateRandomNumberCleaner, '生成随机数'),
    'GEN_SEQUENCE': (GenerateSequenceCleaner, '生成自增序列'),
    'STRIP_UUID': (StripUuidCleaner, '截取UUID'),
    'STRIP_STR': (StripStringCleaner, '截取字符串'),
    'MOCK_ADDR': (MockAddressCleaner, '模拟姓名'),
    'MOCK_CITY': (MockCityCleaner, '模拟城市'),
    'MOCK_ZIPCODE': (MockZipCodeCleaner, '模拟邮编'),
    'MOCK_NAME': (MockNameCleaner, '模拟姓名'),
    'MOCK_COMPANY': (MockCompanyCleaner, '模拟公司名'),
    'MOCK_PHONE': (MockPhoneCleaner, '模拟公司名'),
    'MOCK_SENTENCE': (MockSentenceCleaner, '模拟文本'),
    'MOCK_NUMBER': (MockSentenceCleaner, '模拟数字'),
    'MARK_SIMILARITY': (SimilarityCleaner, '标记相似推荐'),
    'MARK_DATE_COMPARE': (DateCompareCleaner, '标记日期大小'),
}

# 客户类型字典
CUST_TYPE = {
    '普通客户': '系统内',
    '潜力客户': '系统内',
    '亲密客户': '系统内',
    'TOP客户': '系统内',
    'default': '系统外',
}

# 项目类型字典
PROJECT_TYPE = {
    '软件开发': '系统内',
    'default': '系统外'
}

# 项目来源字典
PROJECT_SOURCE = {
    '线索转化': '直接立项',
    '预立项转化': '前置立项',
    'default': '直接立项',
}

# 合同类型字典
CONTRACT_TYPE = {
    '技术': '技术',
    '虚拟合同': '虚拟合同',
    '销售物品': '销售物品',
    '其他': '其他',
    'default': '其他',

}

# 支付方式字典
PAY_TYPE = {
    '2:7:1': '2:7:1',
    '3:3:2:1:1': '3:3:2:1:1',
    '3:3:3.5:0.5': '3:3:3.5:0.5',
    '3:3:3:1': '3:3:3:1',
    '3:5:1:1': '3:5:1:1',
    '3:6:1': '3:6:1',
    '3:7': '3:7',
    'default': '3:7',
}
