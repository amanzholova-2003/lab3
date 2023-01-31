# Amanzholova Assel lab 2
print("Amanzholova Assel lab 2")



def fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)
		

n = 8
fn = 0
fn = fibonacci(n)
print('n = ', fn)
