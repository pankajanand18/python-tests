input=[1,2,100]
counter = 0
input_result=[-1] * 3 
def getStockMax(input,index,current_stocks,current_profit):
	global counter

	print "%s index: %s current_stocks: %s current_profit: %s " % (counter,index,current_stocks,current_profit)
	counter = counter + 1 
	if index  <= len(input)-1:		
		current_value_sell = current_stocks * input[index]

		current_profit = current_profit-(input[index])
		if current_profit < 0:
			current_profit = 0

		next_value_with_buy = getStockMax(input,index+1,current_stocks+1,current_profit)
		next_value_with_sell = getStockMax(input,index+1,0,current_profit+current_value_sell)

		
		return max(max(current_value_sell,next_value_with_buy),next_value_with_sell)
	else:
		return 0 


print getStockMax(input,0,1,0)	


