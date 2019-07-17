def probeHib(seq, p):
	seq = seq.lower()
	p1 = p.lower()

	ml = []
	for i in range(len(seq) - len(p1)):	
		if seq[i] == p1[0]:
			if p1 == seq[i:i+len(p1)] or p1 == seq[i-len(p1):i]:
				ml.append(i)

	if len(ml) != 0:
		return ml
	else:
		return 'no match'

def readFasta(fasta):
	with open(fasta, 'r') as file:
		fastaSeq = ''
		for line in file:
			if line[0] != '>':
				fastaSeq+= line
		print(fastaSeq)
		return fastaSeq

def main():
	seqPath = input('Digite o nome do arquivo .fasta: ')
	s = readFasta(seqPath)
	prob = input('Digite ou cole a sequência do probe:')
	res = probeHib(s, prob)
	if res == 'no match':
		print('Não existem locais de hibridização do probe nesta sequência.')
	else:
		print('O probe hibridiza perfeitamente na(s) posição(ões) {0} da sequência.'.format(', '.join(str(x) for x in res)))

main()