import unittest

from Primes import output_prime_numbers, is_prime

class OutputPrimeTests(unittest.TestCase):
	def test_zero_ten(self):
		self.assertEqual(output_prime_numbers(0, 10), [2, 3, 5, 7])
	def test_minus_ten_to_ten(self):
		self.assertEqual(output_prime_numbers(-10, 10), [2, 3, 5, 7])
	def test_ten_to_0(self):
		self.assertEqual(output_prime_numbers(10, 0), "This thing is wrong")
	def test_twenty_twenty(self):
		self.assertEqual(output_prime_numbers(20, 20), [])
	def tes_typeerror(self):
	        with self.assertRaises(TypeError):
		        raiseError("Wrong Type of Data")
	def works_with_zero(self):
		self.assertEqual(output_prime_numbers(0, 0), [])	
	def test_large_values(self):
		self.asertEquals(output_prime_numbers(0, 100), [2, 3, 5, 7, 11, 13, 15, 17, 19, 23,            29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
	def test_negatives_only(self):
		self.assertEqual(output_prime_numbers(-10, -1), [])
	def test_wrong_type(self):
		self.assertEqual(output_prime_numbers([], []), "Wrong Type of Data")
	def no_float_variables(self):
		self.assertEqual(output_prime_numbers(2.0, 6.4), "Wrong Type of Data" )



