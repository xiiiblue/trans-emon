import utils
from cleaner import RowCleaner

"""
相似度推荐
"""


class SimilarityCleaner(RowCleaner):

    def __init__(self, *args):
        super().__init__(*args)
        if args and len(args) > 0:
            self.threshold = args[0]
        else:
            self.threshold = 0.9

        self.similarity_dict = {}

    def load(self, origin_col_id, repository):
        """
        预处理
        """

        # 遍历Sheet页取原始列
        sentence_dict = {}  # 分词字典 行号:(原始句子,分词数组)
        for row_id in range(repository.title_row_id + 1, repository.row_count):
            # 读取单元格
            cell_value = repository.read_cell(row_id, origin_col_id)

            # 分词
            seg_list = utils.word_segment(cell_value)

            # 加入分词字典
            sentence_dict[row_id] = (cell_value, seg_list)

        # 比较相似度
        self.similarity_dict = self.do_similarity(sentence_dict)

    def clean(self, row_id=None):
        """
        相似度推荐
        """
        if row_id in self.similarity_dict:
            return self.similarity_dict[row_id]

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

                ratio = utils.oc_similarity(src_seg_list, dest_seg_list)
                if ratio > self.threshold:
                    similarity_list.append((ratio, dest_row_id, dest_sentenct))

            # 加入相似度推荐字典
            if similarity_list:
                similarity_text = self.list_to_string(similarity_list)
                similarity_dict[src_row_id] = similarity_text

        return similarity_dict

    @staticmethod
    def list_to_string(similarity_list):
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
