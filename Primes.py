def output_prime_numbers(start, up_to):
	prime_list = []
	
	#checks whether start is greater than upTo
	if start > up_to:
		return "This is wrong data"
	
	#checks whether the data type is correct
	elif type(start) != int or type(up_to) != int:
		return "Wrong Type of Data"

	#returns an empty list in case there's no prime number
	elif start < 2 and up_to < 2:
	  return prime_list
	#Ensures that we start counting up from 2
	elif start <= 2:
		prime_list = [2]
		for num in range(3, up_to + 1, 2):
			if is_prime(num, prime_list):
				prime_list.append(num)
		return prime_list

	elif start % 2 == 0:
		#to save the time and resources, we'll only work with Odd numbers, except "2"
		odd_start = start + 1
		for num in range(odd_start, up_to + 1, 2):
			if is_prime(num, prime_list):
				prime_list.append(num)
		return prime_list

	else:
		for num in range(start, up_to + 1, 2):
			if is_prime(num, prime_list):
				prime_list.append(num)
		return prime_list
		
def is_prime(num, prime_list):
	"""This function is used to determine whether a number is prime or 
	not. To ensure that the code is as efficient as 
	possible, we shall divide num by only the prime numbers that 
	precede it. For example if num is 23, there is no need to test the 
	code from 1 - 23. Only test it on he prime numbers before 23"""
	for prime_num in prime_list:
		if num % prime_num == 0:
			return False
	return True

print(output_prime_numbers(0, 100))

	
