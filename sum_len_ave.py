#############################################################################
## 									   ##
##	Title : Sum + Count + Average					   ##
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# This is a simple program meant to receive input numbers and do a sum of the numbers, count the numbers entered and do an average.
# Use 'done' to escape or terminate the loop after which you should see your results diplayed.

print("\n This is a simple program meant to receive input numbers and do a sum of the numbers entered, count the numbers entered and do an average.\n\n Use 'done' to escape or terminate the program after which you should see your results diplayed.\n\n Let's begin!\n")
		
sum_ = 0
count = 0
average = 0
	
while True:
	
	num_input = input("Enter a number > ")
	
	if num_input == 'done':
		break
	try:
		valid_num = float(num_input)
	
	except:
		print("Enter a valid number!")
		continue
	
	sum_ += valid_num
	
	count += 1
	
	average = sum_/count

print("Total sum is ",sum_ ,"\nTotal number entered is : ", count, "\nThe average is : ", round(average, 3))
