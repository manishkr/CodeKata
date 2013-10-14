class SortFixedRangeNumbers(object):
	def __init__(self, start_num, end_num):
		self.numbers = [0]*(end_num + 1 - start_num)
		self.start = start_num
		self.end = end_num

	def add(self, num):
		if(self.start <= num and num <= self.end):
			self.numbers[num-self.start] += 1

	def get_sorted(self):
		valid_indices = filter(lambda x : self.numbers[x] > 0, range(len(self.numbers)))

		sorted_list = []
		for i in valid_indices:
			sorted_list.extend([i + self.start]*self.numbers[i])

		return sorted_list
