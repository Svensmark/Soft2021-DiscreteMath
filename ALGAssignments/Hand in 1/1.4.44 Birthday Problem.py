import random
import math


def sequencing(N, r):
    sequence = []
    for _ in range(r):
        sequence.append(random.randint(0,N-1))
    return sequence

def validateArray(array):
    #print("Validating given array for repeated numbers: " + str(array))
    count = 1
    for x in array:
        for y in array[count:]:
            if (x == y):     
                return True
        count += 1
    return False

def hypothesis(N):
    #print("Value of N: " + str(N))
    #print("The expected value is: ~" + str(math.sqrt(math.pi*N/2)))
    r = math.ceil(math.sqrt(math.pi*N/2))
    #print("Ceiling of value is: " + str(r))
    return validateArray(sequencing(N,r+5))
    #match = validateArray(sequencing(N,r))
    #if (match):
        #print("A repeated number was found, which has proven that the hypothesis was correct in this case")
    #else:
        #print("No repeated numbers were generated in this sequence.")


def massHypothesis(N, n):
    print("Running the hypothesis " + str(n) + " times ..")
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

N = 365
#hypothesis(N)
n = 1000
massHypothesis(N,n)