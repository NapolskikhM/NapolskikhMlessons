def is_prime(func):
	def wrapper (*args):
		sum_ = func(*args)
		status_ = 'Простое'
		for i in range(sum_ // 2):
			if  i > 1 and sum_ %  i == 0:
				status_ = 'Составное'
				break			
		print(status_)
		return sum_
	return wrapper

@is_prime
def sum_three(a, b, c):
	n = a + b + c
	return n
	
result = sum_three(2, 3, 6)
print(result)
	