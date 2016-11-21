# Program to test for primality error rates
# By: Cameron Clark
import random
# returns True if num is a prime number, false if not
def miller_rabin(num, a):
    s = num - 1
    k = 0
    # Keep halving while s is even
    # k counts how many times we halved
    while s % 2 == 0:
        s = s // 2
        k += 1

    # Miller-Rabin algorithm
    b = pow(a, s, num)
    if b != 1 and b != num - 1:
        j = 1
        while j < k and b != (num - 1):
            b = (b ** 2) % num
            if b == 1:
                return False
            j += 1
        if b != num - 1:
            return False
    return True

if __name__ == '__main__':
    # Get all odd numbers in defined range
    lst = [x for x in range(105000, 115000) if x % 2 == 1]
    # dict to hold our error probabilities
    errors = {}
    # Loop through and check each number
    for num in lst:
        # counts of trues and falses
        true_count = 0
        # try to falsify primalities 20 times
        for x in range(20):
            # Random base
            a = random.randint(2, num - 1)
            r = miller_rabin(num, a)
            if r: true_count += 1
        # if neither are equal to zero it means we had some false positives
        if true_count != 0 and true_count != 20:
            errors[num] = float(true_count)/20.0

    # Get largest error probability
    largest = max(list(errors.values()))
    print("Largest error --> %f" % largest)
    # Print top 10 integers with highest error probability
    print("10 Highest Error Integers:")
    top_lst = sorted(errors, key=errors.get, reverse=True)[:10]
    for x in top_lst:
        print("\t[%d] -- > %f" % (x, errors[x]))
