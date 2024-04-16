# CS124 Programming Assignment 3
# Carlos L. , Aki N.
import math
import heapq
import random

# Input: list of numbers A (example: A = [1,2,3,4])
# Output: Minimum residue

def KarmarkarKarp(A: list) -> int:
    heap = [-num for num in A]
    heapq.heapify(heap)


    # Perform the differencing until only one element remains in the heap
    while (len(heap) > 1):

        # Get the two largest elements
        largest = -heapq.heappop(heap)  
        second_largest = -heapq.heappop(heap)

        # Calculate the difference and push back into the heap if non-zero
        difference = abs(largest - second_largest)
        if (difference > 0):

            # Invert the sign to make it negative (since heapq is a min-heap)
            heapq.heappush(heap, -difference)  

    # The last remaining element is the residue (invert the sign to get the original value)
    final_residue = 0

    if (len(heap) == 1):
        final_residue = -heap[0]

    return final_residue


# TODO: Make correctness tests for repeated random
def RepeatedRandom(A: list, maxIterations: int, representation = 'standard'):
    n = len(A)
    if (representation == 'standard'):
        S = GenerateRandomSolution(n)
        bestResidue = GetResidueStandard(A, S)
        bestSolution = S.copy()

        for _ in range(maxIterations):
            S_new = GenerateRandomSolution(n)
            newResidue = GetResidueStandard(A, S_new)
            if (newResidue < bestResidue):
                bestResidue = newResidue
                bestSolution = S_new.copy()
                S = S_new


    elif (representation == 'prepartition'):
        P = GenerateRandomPrePart(n)
        A_prime = GetAPrime(A, P)
        bestResidue = KarmarkarKarp(A_prime)
        bestSolution = P.copy()
        for _ in range(maxIterations):
            P_new = GenerateRandomPrePart(n)
            A_prime_new = GetAPrime(A, P_new)
            newResidue = KarmarkarKarp(A_prime_new)
            if (newResidue < bestResidue):
                bestResidue = newResidue
                bestSolution = P_new.copy()
                P = P_new
    
    return bestResidue, bestSolution

def HillClimbing(A: list, maxIterations: int, representation = 'standard'):
    n = len(A)
    if (representation == 'standard'):
        S = GenerateRandomSolution(n)
        bestResidue = GetResidueStandard(A, S)
        bestSolution = S.copy()

        for _ in range(maxIterations):
            S_new = GetNeighborStandard(S)
            newResidue = GetResidueStandard(A, S_new)
            if (newResidue < bestResidue):
                bestResidue = newResidue
                bestSolution = S_new.copy()
                S = S_new
    elif (representation == 'prepartition'):
        P = GenerateRandomPrePart(n)
        A_prime = GetAPrime(A, P)
        bestResidue = KarmarkarKarp(A_prime)
        bestSolution = P.copy()
        for _ in range(maxIterations):
            P_new = GetNeighborPrePart(P)
            A_prime_new = GetAPrime(A, P_new)
            newResidue = KarmarkarKarp(A_prime_new)
            if (newResidue < bestResidue):
                bestResidue = newResidue
                bestSolution = P_new.copy()
                P = P_new
    return bestResidue, bestSolution

def simAnneal(A: list, maxIterations: int, representation = 'standard'):
    n = len(A)
    if (representation == 'standard'):
        S = GenerateRandomSolution(n)
        bestResidue = GetResidueStandard(A, S)
        bestSolution = S.copy()

        for t in range(maxIterations):
            S_new = GetNeighborStandard(S)
            newResidue = GetResidueStandard(A, S_new)
            if (newResidue < bestResidue):
                bestResidue = newResidue
                bestSolution = S_new.copy()
                S = S_new
            elif ((math.exp(-(newResidue - bestResidue)/cooling_schedule(t))) > random.random()):
                S = S_new
    elif (representation == 'prepartition'):
        P = GenerateRandomPrePart(n)
        A_prime = GetAPrime(A, P)
        bestResidue = KarmarkarKarp(A_prime)
        bestSolution = P.copy()
        for t in range(maxIterations):
            P_new = GetNeighborPrePart(P)
            A_prime_new = GetAPrime(A, P_new)
            newResidue = KarmarkarKarp(A_prime_new)
            if newResidue < bestResidue:
                bestResidue = newResidue
                bestSolution = P_new.copy()
                P = P_new
            elif math.exp(-(newResidue - bestResidue) / cooling_schedule(t)) > random.random():
                P = P_new
            
    return bestResidue, bestSolution

# HELPER FUNCTIONS

# Input: size of the solution n
# Output: Random solution of size n with S[i] = -1 or 1
def GenerateRandomSolution(n):
    return [random.choice([-1, 1]) for _ in range(n)]

# Input: list of numbers A, list of signs S(olution)
# Output: Residue of the solution
def GetResidueStandard(A: list, S: list)->int:
    sum = 0
    n = len(A)
    for i in range(n):
        sum += A[i] * S[i]
    return abs(sum)


# Input: size of the solution n
# Output: Random pre-partition of size n with S[i] = 1, 2, ..., n (subset an element belongs to)
def GenerateRandomPrePart(n)->list:
    return [random.randint(1, n) for _ in range(n)]

# Input: list of numbers A, list of pre-partition P
# Output: A prime where the elements in the same subset are summed
def GetAPrime(A: list, P: list)->list:
    aPrime = [0] * len(A)

    # Sum the elements in the same subset
    for a, p in zip(A, P):
        aPrime[p - 1] += a

    return aPrime

def GetNeighborStandard(S: list) -> list:
    n = len(S)
    S_new = S.copy()
    index1 = random.randint(0, n - 1)
    index2 = random.randint(0, n - 1)

    while index1 == index2:
        index2 = random.randint(0, n - 1)

    S_new[index1] = -S_new[index1]

    if random.random() < 0.5:
        S_new[index2] = -S_new[index2]

    return S_new


def GetNeighborPrePart(P: list) -> list:
    n = len(P)
    P_new = P.copy()
    index = random.randint(0, n - 1)  
    old_value = P_new[index]
    new_value = random.randint(1, n)
    
    while new_value == old_value:
        new_value = random.randint(1, n)
    
    P_new[index] = new_value
    return P_new

# Chosen cooling schedule (based on recommendation of programming set)
def cooling_schedule(iteration):
    return 10**10 * (0.8 ** (iteration // 300))
