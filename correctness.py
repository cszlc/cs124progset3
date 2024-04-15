from NumPartAlgos import *
from bcolors import *

A = [10, 8, 7, 6, 5]
res_KK = 2

KKalgoRes = KarmarkarKarp(A)
if (KKalgoRes == res_KK):
    print(bcolors.OKGREEN + "Karmarkar-Karp test passed" + bcolors.ENDC)
else:
    print(bcolors.FAIL + "Karmarkar-Karp test failed" + bcolors.ENDC)
    print("Expected: " + str(res_KK))
    print("Got: " + str(KKalgoRes))

