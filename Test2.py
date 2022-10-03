def jujitsu(S, k):
    NewBeginning = S[k:]
    ReversedString = S[::-1]
    NewEnd = ""
    if(k!=0):
        NewEnd = ReversedString[-k:]
    return(NewBeginning + NewEnd)

def checkSequence(S, k):
    Length = len(S)
    print(S[k])
    print(S[Length-(k+1)])
    return(Length/2 > k and S[k] < S[Length-(k+1)])


def extendListByMinMaxElements(L):
    minnimum = min(L)
    maximum = max(L)
    L.remove(minnimum)
    for i in range(minnimum):
        L.append(maximum)
    return

def meiosis(L1, L2, k, j):
    temp = L1[k:j]
    L1[k:j] = L2[k:j]
    L2[k:j] = temp
    return


def repeatIt(S, target, N=1):
    location = S.find(target)
    if(location > -1):
        newString = target * N
        S = S[:location] + newString + S[location:]
    return(S)

def squishIt(S, target):
    targetLength = len(target)
    location = S.find(target)
    return(S[:location] + S[location+targetLength:])

#def fingerprint(w, alpha=printable[10:36]):
 #return(tuple(set(sorted(set(w.lower())))&set(alpha)))

#factorial recursion example
def factorial(n):
    if n ==0:
        return(1)
    return(n * (n-1))

#recursive palidrome example(Not working)
def palindrome(s):
    if len(s) < 2:
        return(True)
    elif s[0] != s[-1]:
        return(False)
    else:
        return(palindrome(s[1:-1]))


