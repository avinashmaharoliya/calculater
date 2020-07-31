print("welcome to my calculator")



print("choose an operator")
print("* , + , - , / ")



c = input("enter the operator")
var1 = int(input("enter first number"))
var2 = int(input("enter second number"))
 
 
if c == '*':
	print("your multiplication is:",var1 * var2)
elif c == '/':
	print("your answer is:",var1 / var2)
elif c == '-':
	print("your subtract is:",var1 - var2)
elif c == '+':
	print("your addtion is:", var1 + var2)
	
else:
		print("enter a valid opertaor")
		
print("thanks for using my calculator")