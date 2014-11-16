

def getString(website_name_orig):
	
	website_name = website_name_orig[4:-4]


	for char in ['a','i','e','o','u']:
		website_name = website_name.replace(char,'')

	length = len(website_name)	
	print website_name
	return "%s/%s"%(length+4,len(website_name_orig))

# print getString("www.google.com")
# print getString("www.o.com")
# print getString("www.hackerearth.com")



t=input()

for i in xrange(t):
	n = raw_input()
	print getString(n)