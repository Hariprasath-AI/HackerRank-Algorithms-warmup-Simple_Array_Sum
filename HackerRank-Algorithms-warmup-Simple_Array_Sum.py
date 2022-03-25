#!/bin/python3

# HackerRank-Algorithms-warmup-Simple_Array_Sum
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum_value = 0
    for i in range(0, len(ar)):
        sum_value += ar[i]
    return sum_value

if __name__ == '__main__':

    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    while ar_count != len(ar):
        print("Size and Number of Inputs Mismatch. Try Again!!")
        ar_count = int(input().strip())
        ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
