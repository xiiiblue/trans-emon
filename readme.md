# TRANS-EMON

## 简介

TRANS-EMON是一个用于Excel方式数据迁移的工具箱，支持多种数据处理策略，支持流水线方式配置化

包含:

- 电话脱敏
- 人名脱敏
- 金额脱敏
- 哈希脱敏
- 分词脱敏
- 分词加哈希脱敏
- 时间格式化
- 相似推荐
- 空白填充
- 全量填充
- 字典替换
- UUID生成

## 使用帮助

TODO

## 命令行示例

```sh
python trans_emon.py --file=/Users/bluexiii/Downloads/export/客户管理20220110103625.xls --config=config/cust.json
```