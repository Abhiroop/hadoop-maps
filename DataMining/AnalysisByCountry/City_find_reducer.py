#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
		line = line.strip()
		
		#line=line.replace(';','\t')
		#print line
    # parse the input we got from mapper.py
		entries = line.split('\t')
		#print entries
		word=entries[0].strip()
		count=entries[-1].strip()
    # convert count (currently a string) to int
		try:
			count = int(count)
		except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
			continue

		if current_word == word:
			current_count += count
        #current_casual+=casual
		else:
			if current_word:
            # write result to STDOUT
				print '%s\t%s' % (current_word, current_count)
			current_count=count
			current_word = word
        #current_casual=casual
      
# do not forget to output the last word if needed!
if current_word == word:
	print '%s\t%s' % (current_word, current_count)
