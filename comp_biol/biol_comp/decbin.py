def decToBin(n):
	bin = []
	while n > 0:
		r = n % 2
		n = n // 2
		bin.append(r)
		print(r, n)
	bin = str(bin[::-1])
	print(bin.replace(",", ""))

num = int(input("Digite um numero decimal: "))
decToBin(num)