#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
current_count = 0
current_casual=0
word = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
  # parse the input we got from mapper.py
	line=line.replace(';','\t')
	entries = line.split('\t')
	word=entries[0].strip()
	count=entries[2]
	casual=int(entries[1])
  # convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
		continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
		current_casual+=casual
	else:
		if current_word:
          # write result to STDOUT
			print '%s\t%s\t%s' % (current_word, current_count,current_casual)
		current_count = count
		current_word = word
		current_casual=casual
# do not forget to output the last word if needed!
if current_word == word:
	print '%s\t%s\t%s' % (current_word, current_count,current_casual)
