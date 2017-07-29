# coding:utf-8
import re

str = "Type3Tag 'FeliCa Standard (RC-S???)' ID=01100410F2145B01 PMM=100B4B428485D0FF SYS=0003"
pattern = "(.*)ID=(\w+)"
match = re.search(pattern, str)

if match is None:
	print 'Not match'
else:
	print (match.group(2))
