import random
import math


def sequencing(N, r):
    sequence = []
    for _ in range(r):
        sequence.append(random.randint(0,N-1))
    return sequence


def calculateHarmonicNumber(N):
    H_n = 0
    for x in range(N):
        x += 1
        H_n += 1/x
    return H_n


def validateArray(N, array):
    result = [None] * N
    count = 0
    for x in array:
        if (x != result[x]):
            result[x] = x
            count += 1
            if (count == len(result)):
                return True
    return False


def hypothesis(N):
    r = math.ceil(N*calculateHarmonicNumber(N))
    return validateArray(N,sequencing(N,r))


def massHypothesis(N, n):
    print("Running the hypothesis " + str(n) + " times ..")
    print("The number of intergers generated is: " + str(math.ceil(N*calculateHarmonicNumber(N))))
    successes = 0
    failures = 0
    for _ in range(n):
        if(hypothesis(N)):
            successes += 1
        else:
            failures += 1
    print("Result:")
    print("Amount of successes in hypothesis: " + str(successes))
    print("Amount of failures in hypothesis: " + str(failures))

massHypothesis(50,1000)