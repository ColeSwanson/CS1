import math

 # fuction example
def function():
    return("hello world")

 # dictionary example
test = {'a':1, 'c':3, 'b':2}

print(test['b'])

 # range example
Numbers = range(2, 6)
print('Numbers at 2 =',Numbers[2])

 #comprehensions (don't work on string)
{print(x,y) for x in range(3) for y in range(3)}

{print(x.upper()) for x in "testing"}

#list L of intigers where a new list is returned containging all elements raised to power K
def mapExponent(L, k):
    return[i**k for i in L]

#Collect list of elements where max is devisible of k
def collectDivisible(max, k):
    return[i for i in range(1, max+1) if i%k == 0]

#Collect letters and lowercase only upercase characters in a string
def spliceUppers(S):
    return(''.join([c.lower() for c in S if c.isupper()]))

#create dictionary with keys are characters and value is number of times that character appears
def countChars(S):
    return({c:S.lower().count(c) for c in set(S.lower()) if c!=' '})

#returns True if a string W is a palidnrome
def palidrome(W):
    return( all( [W[i].lower() == W[-i-1].lower() for i in range(len(W)//2) ]))

#return intiger with only odd characters
def smooshOdds(n):
    
    if (''.join([str(integer) for integer in [int(i) for i in str(n)] if integer%2 == 1])) == '':
        solve = None
    else:
        solve = int(''.join([str(integer) for integer in [int(i) for i in str(n)] if integer%2 == 1]))
    return(solve)

#return true for vowels in a string
def vPattern(S):
    return[S.lower()[i] == "a" or S.lower()[i] == "e" or S.lower()[i] == "i" or S.lower()[i] == "o" or S.lower()[i] == "u" for i in range(len(S))]

#makes possible combinations of intiger characters string characters and temple characters
def combine(I, S, T):
    return[(int(i),s,t) for i in set(str(I)) for s in set(S) for t in set(T)]

#return dictionary of characters in taget as keys and key values are apeareces of key in string
def countEm(S, target):
    return{k:(S.lower().count(k)) for k in set(target.lower()) if S.lower().count(k)>0}

#returns a new string consisting of the first k characters of each word in S, provided that word contains the letter c, independent of case.
def collectIncipits(S, k, c):
    return(' '.join([string[:k] for string in S.lower().split() if string.count(c.lower()) != 0]))

#recursion example (must include conditonal)
def sum(L):
    if L == []:
        return(0)
    return(L[0] + sum(L[1:]))

#return dictionary of string with word as key and dictionary of vowel as key and number of apearances as key value, as key value
def countVowels(S, vowels='aeiou'):
    return{word.lower():{v:word.lower().count(v) for v in set(vowels) if word.lower().count(v) > 0} for word in S.split()}

#recursion example(factorial)
def factorial(n):
    if n == []:
        return(1)
    return(n * factorial(n-1))