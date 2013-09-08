import unittest
import time

class TestCase(object):
    def __init__(self):
        self.file = ""
        self.size = 0
        self.comp_words = []
        
class TestWordProcessor(unittest.TestCase):
    def setUp(self):
        self.case0 = TestCase()
        self.case1 = TestCase()
        
        self.case0.file = "./unittest.txt"
        self.case0.size = 8
        self.case0.comp_words = [('great', 'est', 'greatest'),('smart','est', 'smartest')]
        
        self.case1.file = "./../Anagrams/wordlist.txt"
        self.case1.size = 6
    
    def test_comp_words_fast(self):
        from CompositeWordFast import CompWordProcessor
        self.do_test(CompWordProcessor, self.case0)
    
    def test_comp_words_readable(self):
        from CompositeWordReadable import CompWordProcessor
        self.do_test(CompWordProcessor, self.case0)
    
    def test_time_comparision(self):
        from CompositeWordFast import CompWordProcessor as compWordFast
        from CompositeWordReadable import CompWordProcessor as compWordReadable
        
        word_set_fast_result, fast_result_time = self.do_test_with_time(compWordFast, self.case1)
        word_set_read_result, read_result_time = self.do_test_with_time(compWordReadable, self.case1)
        
        self.assertEqual(word_set_fast_result, word_set_read_result)
        #self.assertLessEqual(fast_result_time, read_result_time, "Fast time is greater than read time")
        
    def do_test_with_time(self, word_processor, test_case):
        start_time  = time.clock()
        word_proc = word_processor(self.case1.file)
        comp_word_set = word_proc.find_composite_words(self.case1.size)
        end_time = time.clock()
        
        time_diff = end_time - start_time
        
        return comp_word_set, time_diff
        
    def do_test(self, wordProcessor, test_case):
        word_proc = wordProcessor(test_case.file)
        comp_word_set = word_proc.find_composite_words(test_case.size)
        self.assertEqual(set(test_case.comp_words), comp_word_set)
        

if __name__ == '__main__':
    unittest.main()   