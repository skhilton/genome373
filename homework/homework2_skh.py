import sys

codon = sys.argv[1]
ok_nucs = 'augcAUGC'
if  len(codon) != 3:
    print('Error! Invalid input!')
elif codon[0] not in ok_nucs or codon[1] not in ok_nucs or codon[2] not in ok_nucs:
    print('Error! Invalid input!')
elif codon.upper() == 'AUG':
    print('Start')
elif codon.upper() == 'UAA' or codon.upper() == 'UAG' or codon.upper() == 'UGA':
    print('Stop')
else:
    print('Amino acid')
