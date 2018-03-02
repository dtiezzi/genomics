import random

def generateReads(genome, numReads, readLen):
	reads= []
	for _ in range(numReads):
		start= random.ranint(0, len(genome) - readLen) - 1
		read.append(genome[star: start + readLen])
	return reads
