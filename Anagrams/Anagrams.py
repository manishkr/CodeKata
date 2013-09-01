import sys
if len(sys.argv) > 0 :
	anagrams = {}
	with open(sys.argv[1], 'r') as file:
		list(map(lambda x: anagrams.setdefault(''.join((sorted(x.strip().lower()))), set()).add(x.strip()), file))

	list(map(lambda x : print(x), anagrams.values()))
