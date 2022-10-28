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
	
while True:
	num_input = input("Enter a number > ")
		
	if num_input == 'done':
		
		break
	try:
		
		valid_num = int(num_input)
	
	except:
		
		print("Enter a valid number!")
		
		continue
			
	num_list = []
		
	num_list.append(valid_num)
		
	for i in num_list:
		count += 1
			
		sum_ += i
			
		average = sum_/count
		
print("Total sum is ",sum_ ,"\nTotal number entered is : ", count, "\nThe average is : ", round(average, 3))
	
#except:
	#print("Kindly enter a valid input 😐️ !")
