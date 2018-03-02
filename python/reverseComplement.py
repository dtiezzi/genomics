def reverseComplement(s):
	if s.find('U') < 0:
		complement = {'A':'T', 'T':'A', 'C': 'G', 'G': 'C', 'N': 'N'}
		t= ''
		for base in s:
			t= complement[base] + t
		return t

	else:
		complement = {'U':'A', 'A':'U', 'C': 'G', 'G': 'C', 'N': 'N'}
		t= ''
		for base in s:
			t= complement[base] + t
		return t
	

seq= 'AATTCCGG'

print(reverseComplement(seq))

seq1= 'AAUUCCGG'

print(reverseComplement(seq1))
