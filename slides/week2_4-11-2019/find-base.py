import sys

base = sys.argv[1]
dna = sys.argv[2]

# solution 1
position = dna.find(base)
if position == -1:
  print("{0} does not occur at all.".format(base))
else:
  print("{0} occus in position {1}".format(base, position+1))

# solution 2
if base in dna:
  position = dna.find(base) + 1
  print("{0} occus in position {1}".format(base, position))
else:
  print("{0} does not occur at all.".format(base))
