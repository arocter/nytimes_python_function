# -*- coding: utf-8 -*-

import urllib
import json
import sys
import time
import random

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


keyword = sys.argv[1]

headlines = list()
headline_clist = list()
final = list()


def headline(keyword):

	params = {
		'q': keyword, 
		'api-key': "b97bf29a899b879148acdb806b0c2e7c:16:74877106"
	}

	query_str = urllib.urlencode(params)
	url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?"+query_str

	raw = urllib.urlopen(url).read()
	data = json.loads(raw)
	data = byteify(data)

	for item in data["response"]["docs"]:
		headlines.append(item["headline"]["main"])

	for times in range(2):
		headline_chosen = random.choice(headlines)
		headline_chosen = headline_chosen.strip()
		headline_clist = headline_chosen.split(" ")
		random.shuffle(headline_clist)
		output = " ".join(headline_clist[2:8])
		final.append(output)

 	all = "\n".join(final)
	return all


print headline(keyword)

	
# print(headlines[:2])

