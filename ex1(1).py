#ftiaxnw enan pinaka gia touw prwtous
#gia tous arithous 2 ews 1000 (to 0 kai 1 den mporoun na einai prwtoi),
#an o arithos otan diaireitai me ton eauto tou exei upoloipo miden
#tote den einai prwtos, alliws einai

primes = []
for possiblePrime in range(2, 1000):
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
    if isPrime:
        primes.append(possiblePrime)
largestPrime = max(primes)
smallestPrime = min(primes)
largestDifference = largestPrime - smallestPrime

print('Largest Prime is', largestPrime)
print('Smallest Prime is', smallestPrime)
print('Largest Difference is', largestDifference)
