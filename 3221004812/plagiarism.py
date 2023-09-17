#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jieba
import gensim
import re
import os
import cProfile

jieba.setLogLevel(jieba.logging.INFO)

# 获取指定路径的文件内容
def get_file_contents(path):
    with open(path, 'r', encoding='UTF-8') as f:
        content = f.read()
    return content

# 将读取到的文件内容进行分词，并过滤特殊符号
def filter_content(content):
    words = []
    for word in jieba.lcut(content):
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", word):
            words.append(word)
    return words

# 忽略掉文本的语法和语序等要素，将其仅仅看作是若干个词汇的集合
def convert_corpus(texts):
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    return corpus

# 计算文本相似度
def calc_similarity(text1, text2):
    texts=[text1,text2]
    dictionary = gensim.corpora.Dictionary(texts)
    
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

def main_run_code():
        path1 = input("输入论文原文的文件的绝对路径：")
        path2 = input("输入抄袭版论文的文件的绝对路径：")
        if not os.path.exists(path1):
            print("论文原文文件不存在！")
            exit()
        if not os.path.exists(path2):
            print("抄袭版论文文件不存在！")
            exit()
        save_path = "C:\\Users\\lenovo\\Desktop\\copy\\result.txt"
        content1 = get_file_contents(path1)
        content2 = get_file_contents(path2)
        text1 = filter_content(content1)
        text2 = filter_content(content2)
        similarity = calc_similarity(text1, text2)
        print("文章相似度：%.2f" % similarity)
        #将相似度结果写入指定文件
        f = open(save_path, 'w', encoding="utf-8")
        f.write("python"+" "+"main.py"+" "+path1+" "+path2+" "+"文章相似度： %.2f"%similarity)
        f.close()


# In[ ]:




