#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from plagiarism import short_analyse, ans

class PaperSimilarityTestCase(unittest.TestCase):
    def setUp(self):
        self.original_file = 'orig.txt'
        self.copied_file = 'orig_0.8_add.txt'
    
    def test_short_analyse(self):
        # Call the short_analyse function
        short_analyse(self.original_file, self.copied_file)
        
        # Additional assertions if needed
        # ...
    
    def test_ans(self):
        # Call the ans function
        similarity = ans(self.original_file, self.copied_file)
        
        # Perform assertions to verify the expected similarity value
        expected_similarity = 80  # Assuming the expected similarity is 80%
        self.assertEqual(similarity, expected_similarity, 
            "The calculated similarity doesn't match the expected value.")

# Manually create a TestSuite and add the test cases
suite = unittest.TestSuite()
suite.addTest(PaperSimilarityTestCase('test_short_analyse'))
suite.addTest(PaperSimilarityTestCase('test_ans'))

# Create a test runner
runner = unittest.TextTestRunner()
# Run the tests
result = runner.run(suite)


# In[1]:


import cProfile
import unittest
import os
from plagiarism import filter_content, calc_similarity

class TestTextSimilarity(unittest.TestCase):

    def test_filter_content(self):
        text = "这是一个测试文本，包含一些特殊符号和停用词。"
        result = filter_content(text)
        expected_result = ["测试", "文本", "包含", "特殊", "符号", "停用词"]
        self.assertEqual(result, expected_result)
    
    def test_calc_similarity(self):
        text1 = "这是一篇原始论文。"
        text2 = "这是一篇相似的抄袭论文。"
        similarity = calc_similarity(text1, text2)
        self.assertAlmostEqual(similarity, 0.8, delta=0.05)  # 预测相似度为0.8左右，允许误差为0.05
if __name__ == "__main__":
    unittest.main()


# In[ ]:




