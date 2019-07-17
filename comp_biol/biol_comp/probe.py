def probeHib(seq, p):
	seq = seq.lower()
	p = p.lower()

	# Converter o probe para a sequência
	pnew = []
	for i in p:
		if i == 'a':
			pnew.append('t')
		elif i == 't':
			pnew.append('a')
		elif i == 'c':
			pnew.append('g')
		else:
			pnew.append('c')
	p1 = ''.join(pnew)

	ml = []
	for i in range(len(seq) - len(p1)):
		
		if seq[i] == p1[0]:
			match = 1
			a = 1
			for j in p1[1:]:
				if j == seq[i + a]:
					match+= 1
				a+= 1
			if match == len(p1):
				ml.append(i)
	if len(ml) != 0:
		return ml
	else:
		return 'no match'

def main():
	s = input('Digite ou cole a sequência de DNA: ')
	prob = input('Digite ou cole a sequência do probe:')
	res = probeHib(s, prob)
	if res == 'no match':
		print('Não existem locais de hibridização do probe nesta sequência.')
	else:
		print('O probe hibridiza perfeitamente na(s) posição(ões) {0} da sequência.'.format(', '.join(str(x) for x in res)))

main()
