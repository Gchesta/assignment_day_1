Def output_prime_numbers(start, upTo):
	prime_list = []
	#checks whether start is greater than upTo
	If start > upTo:
		return "This thing is wrong”
	#checks whether the data type is correct
	elif type(start) != int or type(upTo) != int:
		Raise TypeError(“Wrong Type of data”)
	#returns an empty list in case there’s no prime number
	elif start  < 2 and upto < 2:
`		return prime_list
	#Ensures that we start counting up from 2
Elif start < 2:
		Return out_put_primenumbers(2, upTo)
	Else:
		#to save the time and resources, we’ll only work with Odd numbers, except “2”
prime_list = [2]
		For num in range(3, upTo, 2)
			if is_prime(num):
				prime_list.add(num)
		return prime_list

Def is_prime(num):
	#only working with odd numbers starting from 3
	For I in range(3, num, 2):
		If num % I == 0:
			Return False
	Return True
