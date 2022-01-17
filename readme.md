# TRANS-EMON

## 简介
TRANS-EMON是一个用于Excel方式的数据清洗工具箱，支持多种清洗策略，支持流水线配置

## 清洗策略
目前包含6大类，27个数据清洗工具

### 数据脱敏类

- MASK_PHONE 脱敏电话号码
- MASK_NAME 脱敏姓名
- MASK_MONEY 脱敏金额
- MASK_HASH 脱敏为哈希
- MASK_SEG 脱敏为分词
- MASK_SEG_HASH 脱敏为分词加哈希

### 数据模拟类

- MOCK_ADDR 模拟姓名
- MOCK_CITY 模拟城市
- MOCK_ZIPCODE 模拟邮编
- MOCK_NAME 模拟姓名
- MOCK_COMPANY 模拟公司名
- MOCK_PHONE 模拟电话号码
- MOCK_SENTENCE 模拟文本
- MOCK_NUMBER 模拟数字

### 编号生成类

- GEN_UUID 生成UUID
- GEN_NUM 生成随机数
- GEN_SEQUENCE 生成自增序列

### 数据填充类

- FILL_BLANK 空白填充
- FILL_ALL 全量填充

## 数据加工类

- FORMAT_TIME 时间格式化
- DICT_REPLACE 字典替换
- STRIP_UUID 截取UUID
- STRIP_STR 截取字符串

### 附加标记类

- MARK_SIMILARITY 标记相似推荐
- MARK_DATE_COMPARE 标记日期大小
- MARK_CHECK_LIST 标记检查清单
- MARK_DUPLICATE 标记重复数据


## 流水线配置
以下是一个JSON格式的流水线配置示例: 
```json
[
    ["*项目编号", "STRIP_UUID"],
    ["*项目名称", "MASK_SEG_HASH"],
    ["*项目类型", "DICT_REPLACE", {"foo": "bar"}],
    ["*立项申请人", "FILL_BLANK", "张三"],
    ["*所属部门", "FILL_BLANK", "亿云"],
    ["*项目金额", "MASK_MONEY"],
    ["*立项时间", "FORMAT_TIME"],
    ["*计划验收时间", "FILL_ALL", "2000-01-01"],
    ["*计划结项日期", "FORMAT_TIME"],
    ["*计划结项日期", "FILL_BLANK", "2099-12-31"]
]
```
- JSON配置的格式为双重数组，每一行即为一个流水线步骤
- 具体到每个步骤，在二级数组中依次填入以下参数: 1、列名  2、清洗策略  3、附加参数
- 部分策略例如“标记重复”，不会直接修改本单元格，而是在右侧其它单元格上进行标记。例名的格式为"原始例名|目标列表"，中间用管道符分割。
- 部分策略需要传入参数，例如“FILL_BLANK”填充，需要在策略中写入参数。参数可以有一个或多个，直接在数组后方追加即可。

## 应用安装
1. 要求Python3运行环境，简易使用MiniConda

2. 使用setup脚本安装到系统目录，并生成可执行shell脚本
```sh
python setup.py install
```

3. 执行`transemon --help`查看安装是否正确


## 使用帮助
### 命令方式
1. 需要提前通过setup.py进行安装
2. 安装后，直接在任意目录执行:  
```sh
transemon --file=客户管理20220110103625.xls --config=config/cust.json
或
transemon 客户管理20220110103625.xls config/cust.json
```

### 源码方式
1. 源码方式运行与系统命令类似，需要cd进入到源码目录
2. 源码方式的优势是方便调试
```
cd 应用目录
python transemon.py --file=/path/to/客户管理20220110103625.xls --config=/path/to/config/cust.json
```

### 单元测试方式
1. 单元测试方式，不需要单独的JSON，配置上更加快捷
2. 需要PyCharm等IDE，直接在IDE中执行`test`目录下的测试用例即可

UnitTest示例: 
```
def test_pipeline_1(self):
    """
    客户管理
    """
    path = f"/path/to/客户管理20220110103625.xls"
    rules = [
        ["*客户编号", "STRIP_UUID"],
        ["*客户名称", "MASK_SEG_HASH"],
        ["联系人", "MASK_NAME"],
        ["联系人", "FILL_BLANK", "张三"],
        ["电话", "MOCK_PHONE"],
        ["法定代表人", "MOCK_NAME"],
    ]
    pipeline = ExcelPipeline(path, rules)
    pipeline.process()
```