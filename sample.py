######################################################################
# Specification: sumByproduct(i, j) takes two integers, i and j, and
# returns the sum of i and j times the product of i and j.
#
# Example:
#   >>> sumByProduct(-3, 7)
#   -84
#
def sumByProduct(i, j):
    return( (i+j) * (i*j) )

######################################################################
# Specification: extendSequence(S, i, j) takes a sequence, S, and two
# integers, i < len(S) and j >= 0, and returns a (new) sequence
# consisting of S with the last i elements repeated exactly j times.
# Note: your solution should not use if/elif/else; rather it should
# return the value of a single expression.
#
# Examples:
#   >>> extendSequence((1, 3, 5, 6), 2, 3)
#   (1, 3, 5, 6, 5, 6, 5, 6)
#   >>> extendSequence("yes", 1, 10)
#   'yessssssssss'
#
# Hint: beware corner cases.
#
def extendSequence(S, i, j):
    return(S[:len(S)-i] + S[len(S)-i:]*j)

######################################################################
# Specification: spliceEnds(S, i) takes a sequence, S, and an integer,
# i, and returns a (new) sequence consisting of the last i elements of
# S spliced with the first i elements of S.
#
# Note: no assignment is needed: your solution should not use
# if/elif/else, and should function appropriately even if i > len(S):
# in other words, a single expression in the return suffices.
#
# Examples:
#   >>> spliceEnds((1, 3, 5, 6), 2)
#   (5, 6, 1, 3, 5, 6, 1, 3)
#   >>> spliceEnds("0123456", 3)
#   '4560123456012'
#
# Hint: beware corner cases.
#
def spliceEnds(S, i):
    return(S[len(S)-max(i,0):] + S + S[:max(i,0)])

######################################################################
# Specification: eviscerateList(L, i, j) takes a list, L, and two
# integers, i and j, and modifies the list, L, such that j elements
# starting at index location i are surgically removed from L. The
# function should not return any value.
#
# You may assume 0<=i<len(L) and 0<j.
#
# Examples:
#   >>> L=list(range(10))
#   >>> L
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   >>> eviscerateList(L, 6, 2)
#   >>> L
#   [0, 1, 2, 3, 4, 5, 8, 9]
#
def eviscerateList(L, i, j):
    del L[i:(i+j)]
    return(L)

######################################################################
# Specification: nearAnagram(S1, S2) takes two sequences, S1 and S2,
# and returns True if the two sequences are possible anagrams of each
# other.
#
# Recall an anagram is simply a permutation of the characters of one
# string to make another word, such as "servant" and "taverns" (here,
# we'll extend the notion from strings to sequences, including lists
# and tuples).
#
# A "near anagram" are two sequences that share the same length and
# are made of identical elements, but my differ in how many times each
# element occurs.
#
# Example:
#    >>> nearAnagram('taverns', 'servant')
#    True
#    >>> nearAnagram([1, 2, 3, 1], (2, 2, 1, 3))
#    True
#    >>> nearAnagram([1, 2, 3, 1], [3, 2, 1])
#    False
#
# Hint: do not use assignment or conditionals.
#
def nearAnagram(S1, S2):
    set1 = set(S1)
    set2 = set(S2)
    return(len(S1) == len(S2) and set1 == set2)

######################################################################
# Specification: antigram(S1, S2) takes two sequences, S1 and S2, and
# returns True if the two sequences have identical length, identical
# first and last elements, but share no other elements.
#
# Example:
#    >>> antigram('taverns', 'servant')
#    False
#    >>> antigram([1, 2, 3, 1], (1, 7, 4, 1))
#    True
#    >>> antigram([1, 2, 3, 7, 1], [1, 8, 3, 5, 1])
#    False
#
def antigram(S1, S2):
    set1 = set(S1)
    set2 = set(S2)
    return(S1[0] == S2[0] and S1[-1] == S2[-1] and len(S1) == len(S2) and len(set1&set2) <= 2)

######################################################################  
# Specification: invert(L) takes a list L and modifies it by
# exchanging its first and last halves while also reversing the last
# (now first) half. The function should not return any value.
#
# Example:
#   >>> L=list(range(12))
#   >>> invert(L)
#   >>> L
#   [11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
#   >>> L=[]
#   >>> invert(L)
#   >>> L
#   []
#   >>> L=[1, 2]
#   >>> invert(L)
#   >>> L
#   [2, 1]
#
# Hint: no iteration.
#
# Hint: list operations must be destructive.
#
def invert(L):
    L[:len(L)//2], L[len(L)//2:] = L[len(L)//2:][::-1], L[:len(L)//2]
    return(L)

######################################################################
# Specification: Write a function reverseInt(n) that takes a positive
# integer n and returns the integer that has the same digits of n
# but in reverse order.
#
# Example:
#   >>> reverseInt(7102)
#   2017
#   >>> reverseInt(1024)
#   4201
#   >>> reverseInt(100)
#   1
#   >>> reverseInt(5255498)
#   8945525
#
# Hint: it's OK if leading zeros disappear
#
def reverseInt(n):
    return(int(str(n)[::-1]))

######################################################################
# Specification: write a function sumDigits(n) that takes as input an
# integer, n, and returns the sum of the digits of n while respecting
# the sign of n. Your solution should be elegant and concise!
#
# Note: no for/while required; reviewing [PE] C8 is a good idea.
#
# Example:
#   >>> sumDigits(-132248)
#   -20
#   >>> sumDigits(101)
#   2
#   >>> sumDigits(0)
#   0
#   >>> sumDigits(78214905)
#   36
#
def sumDigits(n):
    pass
