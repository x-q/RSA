def encrypt(m, k):

	(e, n) = k
	c = pow(m, e, n)

	return c
