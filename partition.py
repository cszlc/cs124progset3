import sys
from NumPartAlgos import *

# Input
# ./partition flag algorithm inputfile

# Print input args
def main():

    # Ensure right number of arguments
    if (len(sys.argv) != 4):
        print("Usage: ./partition flag algorithm inputfile")
        sys.exit(1)

    # Will always be 0 as per assignment
    flag = int(sys.argv[1])

    # "algorithm" codes
    # Karmarkar-Karp - 0
    # Repeated Random - 1
    # Hill Climbing - 2
    # Simulated Annealing - 3
    # Prepartitioned Repeated Random - 11
    # Prepartitioned Hill Climbing - 12
    # Prepartitioned Simulated Annealing - 13
    algorithm = int(sys.argv[2])

    # Input file is a list of 100 unsorted integers, one on each line
    # Build array A from input file
    fileName = sys.argv[3]
    A = []
    with open(fileName, "r") as f:
        for line in f:
            A.append(int(line))
    

    if (algorithm == 0):
        KK_algoRes = KarmarkarKarp(A)
        print(KK_algoRes)
    elif (algorithm == 1):
        rrResidue, rrSolution = RepeatedRandom(A, 2500)
        print(rrResidue)
    elif (algorithm == 2):
        hcResidue, hcSolution = HillClimbing(A, 2500)
        print(hcResidue)
    elif (algorithm == 3):
        saResidue, saSolution = simAnneal(A, 2500)
        print(saResidue)
    elif (algorithm == 11):
        prrResidue, prrSolution = RepeatedRandom(A, 2500, 'prepartition')
        print(prrResidue)
    elif (algorithm == 12):
        phcResidue, phcSolution = HillClimbing(A, 2500, 'prepartition')
        print(phcResidue)
    elif (algorithm == 13):
        psaResidue, psaSolution = simAnneal(A, 2500, 'prepartition')
        print(psaResidue)
if (__name__ == "__main__"):
    main()