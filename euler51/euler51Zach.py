# INSTUCTIONS 
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import pickle

def getWildCards(num):
    def movingN(num, n):
        wildCards = []
        if n == 1: #sentinal value
            for i in range(len(str(num))):
                listNum = list(str(num))
                listNum[i] = "*"
                wildCards.append("".join(listNum))
            return wildCards
        for i in range(1,len(str(num))):
            start = str(num)[:i-1]
            end = str(num)[i:]
            endStarList = movingN(end, n-1)
            for endStar in endStarList:
                wildCards.append(start+"*"+endStar)
        return wildCards

    wildCards = []
    numLen = len(str(num))
    for i in range(numLen):
        wildCards.extend(movingN(num, numLen-i))

    return wildCards

def getPossible(wildCard):
    # filling in all the possibilites for this wild card returns the possiblites
    # EX: *3 returns 13, 23, 33, 43, 53, 63, 73, 83, 93
    # EX: 56**3 returns 56003,56113,56223,56333,56443,56553,56663,56773,56883,56993
    possible = []
    for i in range(10):
        # *6001 --> 06001 would change the length
        if not(i == 0 and wildCard[0] == "*"):
            possible.append(wildCard.replace("*",str(i)))
    return possible
def primeCount(primes, possible):
    #from the list of numbers how many are prime
    primeCount = 0
    for num in possible:
        if str(num) in primes: #todo isPrime()
            primeCount += 1
    return primeCount

def getPrimeDictionary():
    #only has primes 1 - 1,000,000
    return pickle.load(open('primes.p', 'rb'))

primes = getPrimeDictionary() # todo I want this as a this to isPrime()
tried = set()

GOAL_LENGTH = 7
number = 1
solved = False
while(not solved):
    if str(number) not in primes:
        wildCards = getWildCards(number) # returns a list 
        #print(number)
        for wildCard in wildCards:
            #print(wildCard)

            #to save time
            if wildCard not in tried:
                #print(wildCard)
                tried.add(wildCard)

                possible = getPossible(wildCard) #a list of the possible numbers for this wildCard
                count = primeCount(primes, possible)
                #print(count)
                if count == GOAL_LENGTH: # Solved
                    print("Answer:",number)
                    solved = True
                    break
    
    number += 2