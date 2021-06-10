import os
os.system("")
def text_to_binary_converter():
		class color:
			bold='\033[01m'
			blue='\033[34m'
			gold='\033[33m'
			red='\033[31m'
			green='\033[32m'
			cyan='\033[36m'
			purple='\033[35m'
		print(color.bold,color.cyan,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(color.bold,color.cyan,"         | Made By @'Cybernetics' !!! |")
		print(color.bold,color.cyan,"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(color.bold,color.green,"\t   { Text  >  ASCII  >  Binary }")
		print(color.bold,color.green,"         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(color.bold,color.blue,"Enter Argument: ",end="")
		ASCII_value_from_Table = input()
		ASCII_values = []
		for character in ASCII_value_from_Table:
		   ASCII_values.append(ord(character))
		binary_converted1 = ''.join(format(ord(c), 'b') for c in ASCII_value_from_Table)
		binary_converted = ' '.join(format(ord(c), 'b') for c in ASCII_value_from_Table)
		print(color.bold,color.gold,"The ASCII Representation Is: \n ",ASCII_values)
		print("  The Binary Representation For Each Value Is:\n ","[", binary_converted,"]")
		print("  The Binary Representation Combined Value Is:\n ","[", binary_converted1,"]")
		again()
def again():
	class color:
			bold='\033[01m'
			red='\033[31m'
			cyan='\033[36m'
			purple='\033[35m'
	print(color.bold,color.purple,"Do you want to continue [Y/N]: ",end="")
	user_decision = input().upper()
	if user_decision == 'Y':
		print(color.bold,color.purple,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(color.bold,color.cyan,"Restarted!!!")
		text_to_binary_converter()
	elif user_decision == 'N':
		print(color.bold,color.purple,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("  Good Bye!!!")
	else:
		print(color.bold,color.red,"Invalid Choice!!!")
		again()
text_to_binary_converter()