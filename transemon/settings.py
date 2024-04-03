import os
from transemon.cleaner.common import TimeFormatCleaner, FillBlankCleaner, FillAllCleaner, DictReplaceCleaner, StripUuidCleaner, \
    StripStringCleaner
from transemon.cleaner.compare import DateCompareCleaner
from transemon.cleaner.duplicate import DuplicateCleaner
from transemon.cleaner.generater import GenerateUuidCleaner, GenerateRandomNumberCleaner, GenerateSequenceCleaner
from transemon.cleaner.mark import CheckListCleaner
from transemon.cleaner.masking import NameMaskingCleaner, HashMaskingCleaner, SegMaskingCleaner, SegHashMaskingCleaner, \
    MoneyMaskingCleaner, \
    PhoneMaskingCleaner, HashAllMaskingCleaner
from transemon.cleaner.mock import MockAddressCleaner, MockCityCleaner, MockZipCodeCleaner, MockNameCleaner, MockCompanyCleaner, \
    MockPhoneCleaner, \
    MockSentenceCleaner
from transemon.cleaner.similarity import SimilarityCleaner


def get_settings(var):
    """
    获取配置
    """
    if f'TE_{var}' in os.environ:
        return os.environ.get(f'TE_{var}')
    else:
        if var in SETTINGS:
            return SETTINGS[var]
        else:
            return None


def set_settings(var, val):
    """
    覆盖配置
    """
    os.environ.setdefault(var, str(val))


# 全局默认参数
SETTINGS = {
    'SHEET_IDX': 0,
    'TITLE_ROW': 0,
    'FILE_SUFFIX': "(已清洗)",
}

# 数据清洗器配置
CLEANER = {
    # 数据脱敏类
    "MASK_PHONE": (PhoneMaskingCleaner, "脱敏电话号码"),
    "MASK_NAME": (NameMaskingCleaner, "脱敏姓名"),
    "MASK_MONEY": (MoneyMaskingCleaner, "脱敏金额"),
    "MASK_HASH": (HashMaskingCleaner, "脱敏为哈希"),
    "MASK_HASH_ALL": (HashAllMaskingCleaner, "脱敏为全哈希"),
    "MASK_SEG": (SegMaskingCleaner, "脱敏为分词"),
    "MASK_SEG_HASH": (SegHashMaskingCleaner, "脱敏为分词加哈希"),
    # 数据模拟类
    "MOCK_ADDR": (MockAddressCleaner, "模拟姓名"),
    "MOCK_CITY": (MockCityCleaner, "模拟城市"),
    "MOCK_ZIPCODE": (MockZipCodeCleaner, "模拟邮编"),
    "MOCK_NAME": (MockNameCleaner, "模拟姓名"),
    "MOCK_COMPANY": (MockCompanyCleaner, "模拟公司名"),
    "MOCK_PHONE": (MockPhoneCleaner, "模拟电话号码"),
    "MOCK_SENTENCE": (MockSentenceCleaner, "模拟文本"),
    "MOCK_NUMBER": (MockSentenceCleaner, "模拟数字"),
    # 编号生成类
    "GEN_UUID": (GenerateUuidCleaner, "生成UUID"),
    "GEN_NUM": (GenerateRandomNumberCleaner, "生成随机数"),
    "GEN_SEQUENCE": (GenerateSequenceCleaner, "生成自增序列"),
    # 数据填充类
    "FILL_BLANK": (FillBlankCleaner, "空白填充"),
    "FILL_ALL": (FillAllCleaner, "全量填充"),
    # 数据加工类
    "FORMAT_TIME": (TimeFormatCleaner, "时间格式化"),
    "DICT_REPLACE": (DictReplaceCleaner, "字典替换"),
    "STRIP_UUID": (StripUuidCleaner, "截取UUID"),
    "STRIP_STR": (StripStringCleaner, "截取字符串"),
    # 附加标记类
    "MARK_SIMILARITY": (SimilarityCleaner, "标记相似推荐"),
    "MARK_DATE_COMPARE": (DateCompareCleaner, "标记日期大小"),
    "MARK_CHECK_LIST": (CheckListCleaner, "标记检查清单"),
    "MARK_DUPLICATE": (DuplicateCleaner, "标记重复数据"),
}
