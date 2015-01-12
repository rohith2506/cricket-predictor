fname = open("in.txt","rb")
lst = fname.readlines()

for l in lst:
	temp  = l.split("\">")
	print temp[1].split("</")[0] + "=" + temp[0].split("=\"")[1]
