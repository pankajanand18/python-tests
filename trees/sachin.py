# Question 1: Given a string of words return all words which have their reverse present in the string as ( (word1 , reverseword1 ) , (word2 ,reverseword2) )

# eg .
# Input -   
# Sachin tendulkar is the best   tseb    eth  nihcaS  
input='Sachin tendulkar is the best   tseb    eth  nihcaS'
hash={}
word=''
for char in input:
	print char

	if char == ' ':
		if len(word) > 0:
			word_list= hash.get(len(word),[])
			word_list.append(word)
			hash[len(word)]= word_list

			word=''

	else:
		word = word + char;

hash[len(word)].append(word)




hash

