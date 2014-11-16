coins=[1,2,5,10]

def getDenomination(coins,sum):
	min_deno=[0] * (sum + 1 )

	for amt in xrange(1,sum+1):
		min_deno[amt]= 30000
		temp= 30000
		for i in xrange(len(coins)):
			if amt >= coins[i]:
				temp_amt = min_deno[amt-coins[i]] + 1 
				#print temp_amt
				if temp_amt < temp:
					temp = temp_amt
					min_deno[amt] = temp
			print "%s %s %s"%(coins[i],amt,min_deno)

			

	print min_deno

getDenomination(coins,23)
