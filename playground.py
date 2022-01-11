import jieba

str = '山东省海内外高层次人才服务专家基地信息化平台'

seg_list = jieba.lcut(str)
seg_len = len(seg_list)

if (seg_len < 5):
    plain_positions = [0, seg_len - 1]
elif (seg_len < 10):
    plain_positions = [0, int(seg_len / 2), seg_len - 1]
elif (seg_len < 20):
    plain_positions = [0, int(seg_len / 3), int(seg_len * 2 / 3), seg_len - 1]
else:
    plain_positions = [0, int(seg_len / 4), int(seg_len * 2 / 4), int(seg_len * 3 / 4), seg_len - 1]
print(plain_positions)

result = ''
for idx, word in enumerate(seg_list):
    print(idx, word)

    if idx in plain_positions:
        result += word
    else:
        result += '*' * len(word)

print(result)
