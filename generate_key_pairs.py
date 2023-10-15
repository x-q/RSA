import generate_random_number, miller_rabin, pickle


def extended_gcd(a, b):

	if a == 0:

		return (b, 0, 1)

	else:

		gcd, x, y = extended_gcd(b % a, a)
		return (gcd, y - (b // a) * x, x)


def generate_keys(length):

	'''

	Generate "p"

	'''

	prime = False

	while not prime:

		num = generate_random_number.generate(length - 10)
		prime = miller_rabin.miller_rabin(num)

	prime = False

	i = 2

	while not prime:

		temp = num * i + 1
		prime = miller_rabin.miller_rabin(temp)
		i += 2

	p = temp

	'''

	Generate "q"

	'''

	prime = False

	while not prime:

		num = generate_random_number.generate(length)
		prime = miller_rabin.miller_rabin(num)

	prime = False

	i = 2

	while not prime:

		temp = num * i + 1
		prime = miller_rabin.miller_rabin(temp)
		i += 2

	q = temp

	'''

	Generate "d" by finding a large prime greater than p or q

	'''

	while not prime:

		num = generate_random_number.generate(length + 10)
		prime = miller_rabin.miller_rabin(num)

	prime = False

	i = 2

	while not prime:

		temp = num * i + 1
		prime = miller_rabin.miller_rabin(temp)
		i += 2

	d = temp

	'''

	Generate "e" by using a modified verion of Euclid's GCD Algorithm

	'''

	n = p * q
	phi_n = n - (p + q) + 1
	gcd, e, y = extended_gcd(d, phi_n)
	e = e % phi_n

	return ((d, n), (e, n))
