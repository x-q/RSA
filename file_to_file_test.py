import pickle, encrypt

with open('keys.pickle', 'rb') as source:
	((e, n), (d, n)) = pickle.load(source)

chonk_size = 10

with open('keys.pickle', 'rb') as in_file, open('poopoo', 'wb') as out_file:
	while True:
		chonkerzz = in_file.read(10)

		if chonkerzz == b"":
			break

		length = len(chonkerzz)

		print(chonkerzz)

		secrets = encrypt.encrypt(int.from_bytes(chonkerzz, 'big'), (e, n))

		print(secrets)

		jk = encrypt.encrypt(secrets, (d, n))

		print(jk)
		
		out_file.write(jk.to_bytes(length, 'big'))
