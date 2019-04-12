"""
Molecular Evolution Simulator.

Written by Jim Thomas and Sarah Hilton
April 2019
"""
import sys
import random
import math
import time
from optparse import OptionParser


def main():
    """Process inputs and run simulations."""
    # set up
    (totalAlleles, freqA, fitAA, fitAa, fitaa) = process_arguments()
    print("\nSimulation parameters:")
    print(" There are {0} alleles in the population.\n"
          " The starting A count is {1}\n"
          " The starting a count is {2}\n".format(totalAlleles,
                                                  freqA * totalAlleles,
                                                  totalAlleles * (1 - freqA)))
    print(" The fitness of AA is {0}\n"
          " The fitness of Aa is {1}\n"
          " The fitness of aa is {2}.".format(fitAA, fitAa, fitAa))

    print("\n---------------------")

    # main calculations
    fixedA = 0
    fixedB = 0
    genA = []
    genB = []
    gens = 500  # set by SKH
    print("Running simulation for {0} generations".format(gens))
    pop = Population(totalAlleles/2, freqA, fitAA, fitAa, fitaa)
    for gen in range(gens):
        runGeneration(pop)
        if gen % 100 == 0:
            print("\n Generation {0}. Frequency A {1}. "
                  "Frequency a {2}.".format(gen, pop.numA, pop.numB))
    print("\n Generation {0}. Frequency A {1}."
          "Frequency a {2}.".format(gen, pop.numA, pop.numB))

    print("\n---------------------\n")

    print("Final results:")
    if pop.numB == 0:
        print(" A fixed")
    elif pop.numA == 0:
        print(" a fixed")
    else:
        print(" Neither A nor a fixed.")


# Define a class called population
class Population:
    """Define population class."""
    def __init__(self, popSize, freqA, fitAA, fitAa, fitaa):
        """Init."""
        self.popSize = popSize
        self.numA = round(2 * popSize * freqA)
        self.numB = 2 * popSize - self.numA
        self.fitAA = fitAA
        self.fitAa = fitAa
        self.fitaa = fitaa


# key function
def runGeneration(pop):
    """Run a single generation."""
    if pop.numA == 0 or pop.numB == 0:
        return
    freqA = float(pop.numA) / (2 * pop.popSize)
    numA = 0
    numB = 0
    # keep adding alleles drawn from old population until
    # new population is the same size as the old
    # the number of times through the loop is indeterminate
    # because selection may remove individuals
    while numA + numB < 2 * pop.popSize:
        case = 1  # AA by default, changed if draw calls for it
        if random.random() < freqA:  # keep first A
            if random.random() >= freqA:
                case = 2  # Aa (else AA)
        else:  # keep first a
            if random.random() < freqA:
                case = 2  # aA
            else:
                case = 3  # aa
        # impose selection if needed
        if case == 1 and pop.fitAA < 1.0 and random.random() >= pop.fitAA:
            continue  # dead genotype
        elif case == 2 and pop.fitAa < 1.0 and random.random() >= pop.fitAa:
            continue  # dead genotype
        elif case == 3 and pop.fitaa < 1.0 and random.random() >= pop.fitaa:
            continue  # dead genotype
        if case == 1:
            numA += 2
        elif case == 2:
            numA += 1
            numB += 1
        else:
            numB += 2
    # next generation allele population is drawn, set it in the class members
    pop.numA = numA
    pop.numB = numB
    return None


def process_arguments():
    """Process command line arguments."""
    oparser = OptionParser()
    oparser.add_option("--pop", type="int", dest="totalAlleles", default="1000",
                       help="Total number of alleles")
    oparser.add_option("--freq", "--startFreqA", type="float", dest="freqA",
                       default="0.5", help="frequency of starting A alleles, "
                       "default %default")
    oparser.add_option("--fAA", type="float", dest="fitAA", default="1.0",
                       help="fitness of AA, default %default")
    oparser.add_option("--fAa", type="float", dest="fitAa", default="1.0",
                       help="fitness of Aa, default %default")
    oparser.add_option("--faa", type="float", dest="fitaa", default="1.0",
                       help="fitness of aa, default %default")
    (opt, args) = oparser.parse_args(sys.argv)

    # check args
    if opt.fitAA > 1 or opt.fitAA < 0 or opt.fitAa > 1 or opt.fitAa < 0 or opt.fitaa > 1 or opt.fitaa < 0:
        raise ValueError("Error: Fitnesses must be between 0 and 1 "
                         "not {0} {1} {2}".format(fitAA, fitAa, fitaa))
    if opt.freqA > 1 or opt.freqA < 0:
        raise ValueError("Error: The starting frequency of A must be between "
                         "0.0 and 1.0 not {0}".format(opt.freqA))
    return opt.totalAlleles, opt.freqA, opt.fitAA, opt.fitAa, opt.fitaa

if __name__ == '__main__':
    main()
