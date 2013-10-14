class SortChars(object):
	ascii_offset = ord('a')
	total_chars = 26
	def __init__(self):
		self.char_counts = [0]*self.total_chars
		self.char_range = range(0, self.total_chars)

	def add(self, chars):
		lower_chars = chars.lower()
		for c in lower_chars:
			num = ord(c) - self.ascii_offset
			if num in self.char_range:
				self.char_counts[num] += 1

	def get_sorted(self):
		valid_indices = filter(lambda x : self.char_counts[x] > 0, self.char_range)

		sorted_chars = []
		for i in valid_indices:
			sorted_chars.extend([chr(i + self.ascii_offset)]*self.char_counts[i])
			
		sorted_chars = "".join(sorted_chars)

		return sorted_chars
