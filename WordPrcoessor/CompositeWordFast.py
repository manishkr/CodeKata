class CompWordProcessor(object):
    def __init__(self, word_file):
        self.__word_map = {}
        with open(word_file) as file:
            list(map(lambda x: self.__word_map.setdefault(len(x.strip()), set()).add(x.strip()), file))
            
    def __process(self, size, pair_exist):
        comp_words = set()
        size_set = self.__word_map.setdefault(size)
        
        for key in pair_exist:
            left_set = self.__word_map[key]
            right_set = self.__word_map[size-key]
            
            for word in size_set:
                if((word[0:key] in left_set) and (word[key:size] in right_set)):
                    comp_words.add((word[0:key], word[key:size], word))
        
        return comp_words
            
    
    def find_composite_words(self, size):
        less_than_size = filter(lambda x : x < size, self.__word_map.keys())
        pair_exist = filter(lambda x : size - x in self.__word_map.keys(), less_than_size)
               
        comp_words = self.__process(size, pair_exist)
        
        return comp_words
        
        
            
        