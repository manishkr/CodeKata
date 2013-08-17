if !ARGV.empty?
	anagrams = Hash.new{|h, k| h[k] = []}
	IO.foreach(ARGV[0]){|w| anagrams[w.strip.downcase.chars.sort.join].push(w.strip)}
	anagrams.values.each{|v| print v, "\n"}
end

