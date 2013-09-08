class CompWordProcessor(object):
    def __init__(self, word_file):
        self.__word_map = {}
        with open(word_file) as file:
            for line in file:
                word = line.strip()
                len_word_set = self.__word_map.setdefault(len(word), set())
                len_word_set.add(word)
            
    def __process(self, size, pair_exist):
        comp_words = set()
        size_set = self.__word_map.setdefault(size)
        
        for key in pair_exist:
            left_set = self.__word_map[key]
            right_set = self.__word_map[size-key]
            
            for word in size_set:
                left_word = word[0:key]
                right_word = word[key:size]
                
                if((left_word in left_set) and (right_word in right_set)):
                    comp_words.add((left_word, right_word, word))
        
        return comp_words
            
    
    def find_composite_words(self, size):
        pair_exist = []
        for key in self.__word_map.keys():
            if (size - key) in self.__word_map.keys():
                pair_exist.append(key)
                
        comp_words = self.__process(size, pair_exist)
        
        return comp_words