"""
Example solutions for HW6.

SKH 20190523
"""
import sys


def count_nucleotides(sequence):
    """Count nucleotdies in a sequence."""
    nt_dict = {"A": sequence.count("A"),
               "C": sequence.count("C"),
               "T": sequence.count("T"),
               "G": sequence.count("G")
               }
    return nt_dict


def gc_content(nuc_counts):
    """Calculate GC content."""
    gc = (nuc_counts["G"] + nuc_counts["C"])
    gc = gc / (gc + nuc_counts["A"] + nuc_counts["T"])
    return gc


def strategy_one():
    """Readlines and while loops.

    In this function, the output file is opened using a `while` loop and the
    input data is read using `readlines()`. The sequence name is distinguished
    from the `sequence` using `.startswith(">")`
    """
    # read in from the command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # open the data
    data = open(input_file, "r")
    data = data.readlines()

    # process the data
    with open(output_file, "w") as f:
        for line in data:
            if line.startswith(">"):  # fasta header
                f.write(line.strip())  # write the sequence name
            else:
                # remove new line, make all uppercase
                nts = count_nucleotides(line.strip().upper())
                gc = gc_content(nts)
                f.write(" {0}\n".format(round(gc, 3)))  # add space then GC


def strategy_two():
    """Readlines but no while loops.

    This function is identical to the one above *except* for how the writing to
    the output file is handled.

    The output file is opened before the `for` loop and closed after.
    """
    # read in from the command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # open the data
    data = open(input_file, "r")
    data = data.readlines()

    # open output file
    f = open(output_file, "w")

    for line in data:
        if line.startswith(">"):
            f.write(line.strip())  # write the sequence name
        else:
            # remove new line, make all uppercase
            nts = count_nucleotides(line.strip().upper())
            gc = gc_content(nts)
            f.write(" {0}\n".format(round(gc, 3)))

    # close the output file
    f.close()


def strategy_three():
    """Every other for loop.

    In this function, the sequence names and sequences are extracted in one
    loop iteration. The loop goes over the odd numbers (sequence names) and the
    sequences are indexed by `i + 1`.
    """
    # read in from the command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # open the data
    data = open(input_file, "r")
    data = data.readlines()

    with open(output_file, "w") as f:
        for i in range(0, len(data), 2):  # only the odd numbered lines
            seq_name = data[i].strip()  # odd lines are sequence names
            seq = data[i+1].strip()  # even lines are sequences
            nts = count_nucleotides(seq.strip().upper())
            gc = gc_content(nts)
            f.write("{0} {1}\n".format(seq_name, round(gc, 3)))


def strategy_four():
    """Readline.

    This function uses `readline()` instead of `readlines()` to grab the
    sequence name and the sequence at the same time.
    """
    # read in from the command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # open the data
    data = open(input_file, "r")

    with open(output_file, "w") as f:
        while True:  # go until the file is empty
            seq_name = data.readline().strip()  # first line is the name
            if len(seq_name) == 0:  # is the file empty?
                break
            seq = data.readline().strip()  # the second line is the sequence
            nts = count_nucleotides(seq.strip().upper())
            gc = gc_content(nts)
            f.write("{0} {1}\n".format(seq_name, round(gc, 3)))
