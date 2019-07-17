def primeiroDuplicado(l):
	v = 0
	if len(set(l)) == len(l):
		v = -1
		print(v)
	else:
		for x, i in enumerate(l):
			c = x + 1
			for j in (l[x+1:]):
				if i == j:
					v = c
				c+=1
		print(l[v])

l1 = [2, 4, 3, 5, 1]

primeiroDuplicado(l1)