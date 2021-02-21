# -*- coding:utf-8 -*-

"""词频统计"""
import jieba
from collections import Counter


def word_count(string):
    seg = jieba.cut(string*20, cut_all=False)
    wc_dict = dict(Counter(list(seg)).items())

    n = ["，", "。", "！", "？", ".", " ", "?", "、", "…", "!"]
    for i in n:
        if wc_dict.get(i, None):
            del wc_dict[i]
    return wc_dict

if __name__ == "__main__":
    word_count("哈哈哈,行啊.哈哈  经典蓝赛铃风  s法定  sdk凡灵")