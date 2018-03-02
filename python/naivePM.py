# This is the naive function for perfect match in genome

def naive(p, t):    #p= pattern anf t= test to search
	occurences= []
	for i in range(len(t) - len(p) + 1):
		match= True
		for j in range(len(p)):
			if not t[i+j] == p[j]:
				match= False
				break
		if match:
			occurences.append(i)
	return occurences

p= 'ACG'
t= "AGCTGAGTTGACGTT"

print(naive(p,t))
