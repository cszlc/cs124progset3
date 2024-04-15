# CS124 Programming Assignment 3
# Carlos L. , Aki N.

import heapq

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

