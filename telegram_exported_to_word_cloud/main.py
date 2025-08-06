import json
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

remove_list = ["，","*",] # 在词云里忽略的词

source_list = []  # 从json文件里处理出来的文本
segmentation_list = []  # 分词的结果


def read_from_source() -> None:
    # 读取 JSON 文件
    with open("result.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 提取文本内容
    for message in data.get("messages", []):
        if message.get("type") == "message":
            for entity in message.get("text_entities", []):
                if entity.get("type") == "plain":
                    source_list.append(entity.get("text"))


def segmentation():
    for str in source_list:
        segmentation_list.append(jieba.lcut(str, cut_all=False))


def count_words_and_draw():
    flat_list = [
        item.replace("\n", "")
        for sublist in segmentation_list
        for item in sublist
        if item.strip() != "" and item not in remove_list
    ]
    word_counts = Counter(flat_list)
    print(word_counts)
    wc = WordCloud(
        font_path="/System/Library/Fonts/STHeiti Light.ttc",  # 中文需要指定字体路径
        width=1400,
        height=800,
        background_color="white",
    ).generate_from_frequencies(word_counts)

    # 显示词云
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    read_from_source()
    segmentation()
    count_words_and_draw()
