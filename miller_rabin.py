import random

# hyperparameter
k = 120

def miller_rabin(num):

	prime = True

	if num % 2 == 0:

		return False

	one_less = num - 1
	s = 1
	modulus = 0

	while modulus == 0:

		modulus = one_less % (2 ** s)

		if modulus == 0:

			s += 1

	s -= 1
	d = one_less // (2 ** s)

	for runs in range(k):

		prime_test = False
		a = random.randint(2, num - 2)

		for e in range(s):

			result = pow(a, (2 ** e) * d, num) #result = modular_arithmetic.power(a, (2 ** e) * d, num)

			if (e == 0 and result == 1) or result == num - 1:

				prime_test = True

			else:

				continue

		if not prime_test:

			prime = False

	return prime
