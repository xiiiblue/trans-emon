import jieba
from processor import Processor


# from settings import THRESHOLD


class SimilarityProcessor(Processor):
    """
    相似度推荐
    """

    def __init__(self, *args):
        self.threshold = args[0]
        print(f'threshold: {self.threshold}')

    def process(self, origin):
        pass

    def pre_process(self, origin_col_id, repo):
        """
        预处理
        """

        # 遍历Sheet页取原始列
        sentence_dict = {}  # 分词字典 行号:(原始句子,分词数组)
        for row_id in range(repo.title_row_id + 1, repo.row_count):
            # 读取单元格
            cell_value = repo.read_cell(row_id, origin_col_id)

            # 分词
            seg_list = jieba.lcut(cell_value.strip())

            # 剔除特殊字符
            for seg in seg_list:
                if self.is_symbol(seg):
                    seg_list.remove(seg)

            # 加入分词字典
            sentence_dict[row_id] = (cell_value, seg_list)

        # 比较相似度
        self.similarity_dict = self.do_similarity(sentence_dict)

    def process_by_id(self, row_id):
        """
        相似度推荐
        """

        if row_id in self.similarity_dict:
            return self.similarity_dict[row_id]

    def is_symbol(self, char):
        """
        判断是否为特殊字符
        """
        symbols = "~!@#$%^&*()_+-*/<>,.[]\/（）【】，。《》"
        for symbol in symbols:
            if char == symbol:
                return True
        return False

    def oc_similarity(self, list_a, list_b):
        """
        判断相似度(Overlap Coefficient算法)
        """
        set_a = set(list_a)
        set_b = set(list_b)
        set_c = set_a.intersection(set_b)
        return float(len(set_c)) / float(min(len(set_a), len(set_b)))

    def do_similarity(self, sentence_dict):
        """
        比较相似度
        """
        # 相似度推荐字典
        similarity_dict = {}

        # 比较相似度
        for src_row_id, (src_sentenct, src_seg_list) in sentence_dict.items():
            similarity_list = []  # 相似行内容数组
            for dest_row_id, (dest_sentenct, dest_seg_list) in sentence_dict.items():
                if src_row_id == dest_row_id:
                    continue

                ratio = self.oc_similarity(src_seg_list, dest_seg_list)
                if ratio > self.threshold:
                    similarity_list.append((ratio, dest_row_id, dest_sentenct))

            # 加入相似度推荐字典
            if similarity_list:
                similarity_text = self.similarity_list_to_string(similarity_list)
                similarity_dict[src_row_id] = similarity_text

        return similarity_dict

    def similarity_list_to_string(self, similarity_list):
        """
        相似列表转文本
        """
        text = ''
        for row in similarity_list:
            ratio, dest_row_id, dest_sentence = row
            if text:
                text += '  |  '
            text += f'{dest_sentence}  相似度:{ratio}  行号:{dest_row_id + 1}'
        return text
