#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cProfile
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
cProfile.run('main_run_code()')
if __name__ == '__main__':
    main_run_code()


# In[ ]:




