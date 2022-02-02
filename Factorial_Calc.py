def factorial(x):
	if x==1:
		return 1
	else:
		return (x* factorial(x-1))
		
num = int((input ("Pick a number to find the factorial of\n")))
print("\n\nThe factorial of", num, "is", factorial(num))
