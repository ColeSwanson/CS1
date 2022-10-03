# CS1210: Lab3 [4 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partners, and
#  2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the words "hawkid1" and "hawkid2" between the two
# double quote marks to match your own hawkids. Your hawkid is the
# "login identifier" you use to login to all University services, like
# `https://myUI.uiowa.edu/'
#
# Note: we are not asking for your passwords, just the login
# identifiers: for example, mine is "segre".
#
# Note: if there are 3 of you, add a third string to the list returned.
#
def signed():
    return(["ctswanson","ngadelha"])

######################################################################
# Note: Starting with Lab3, I am providing fewer test cases for each
# function. Here, we are only checking the type of your output and the
# solution to one sample problem. You should feel free to define your
# own test cases to ensure your solution meets the specification.
######################################################################
# Specification: fingerprint(w) takes a string or word, w, and
# produces a sorted tuple containing all of the characters present in
# the word, with duplicates excluded. Note that non-alphabetic
# characters should be dropped, and upper case characters should be
# treated as if they were lower case.
#
# Example:
#   >>> fingerprint('goldfish')
#   ('d', 'f', 'g', 'h', 'i', 'l', 'o', 's')
#   >>> fingerprint('strawberry')
#   ('a', 'b', 'e', 'r', 's', 't', 'w', 'y')
#   >>> fingerprint('Pelham123')
#   ('a', 'e', 'h', 'l', 'm', 'p')
#
# Note: The default definition of the alpha argument is as it was in
# printVowel() from lab2.
from string import printable
#
# Hint: For full credit function should consist of a single statement;
# neither conditionals nor iteration are needed to solve the problem.
# Also, you may wish to review the Python sorted() function, mentioned
# briefly in [PE] C8; how does this differ from the list.sort()
# method?
#
def fingerprint(w, alpha=printable[10:36]):
    return(tuple(set(sorted(set(w.lower())))&set(alpha)))

######################################################################
# Specification: anagramish(w1, w2) takes two strings or words, w1 and
# w2, and returns True if they are "sort of anagrams." For this
# problem, "sort of anagrams" means they are the same length and have
# the same fingerprint(), as defined above.
#
# Example:
#   >>> anagramish('Pelham123', 'hamapleah')
#   True
#   >>> anagramish('Orchestra', 'carthorse')
#   True
#   >>> anagramish('racecar', 'career')
#   False
#
def anagramish(w1, w2):
    return(len(w1) == len(w2) and fingerprint(w1) == fingerprint(w2))

######################################################################
# Specification: repeatIt(S, target, N) takes a string, S, a target
# string, target, and an integer, N, and returns a new version of the
# string with the first occurrance of target within the original
# string S replicated N times. If target is not in S, then you should
# just return S unchanged. Ignore case when detecting target within S.
#
# Example:
#   >>> repeatIt('The rain in Spain', 'IN ', 2)
#   'The rain in in Spain'
#   >>> repeatIt("Rollin', keep them dawgies rollin'", "rollin', ", 3)
#   "Rollin', Rollin', Rollin', keep them dawgies rollin'"
#   >>> repeatIt('You look wonderful, tonight', 'full', 4)
#   'You look wonderful, tonight'
#
# Hint: For this problem, my solution uses both assignment and
# conditionals; you should feel free to do so as well.
#
# Note: You might want to reviewed [PE] C3 and C6.
#
def repeatIt(S, target, N=1):
    location = S.find(target)
    if(location > -1):
        newString = target * (N-1)
        S = S[:location] + newString + S[location:]
    return(S)

######################################################################
# Specification: collapseIt(S, target) takes a string, S, and a target
# string, target, and returns a new copy of S with all occurrences of
# target removed.  Note that unlike repeatIt(), case matters here.
#
# Example:
#   >>> squishIt('The rain in Spain', ' ')
#   'TheraininSpain'
#   >>> squishIt('The rain in Spain', 'in')
#   'The ra  Spa'
#   >>> squishIt('The rain in Spain', 'FOO')
#   'The rain in Spain'
#
# Hint: You might want to review [PE] C6.
#
def squishIt(S, target):
    return(S[:S.find(target)] + S[S.find(target)+len(target):])

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__':
    if type(signed()) is not list:
        print('### Error: Do not alter signed() other than to replace hawkid with your own.')
        exit()
    if len(signed()[0]) >= 6 and signed()[0][6] == "hawkid":
        print('### Error: Replace the 6 characters in "hawkid" with your own hawkids in the signed() function.')
        exit()

    if not isinstance(fingerprint("foo"), tuple):
        print("### Error: your definition of fingerprint(w) does not return a tuple.")
        exit()
    elif (fingerprint("F00bar") != ('a', 'b', 'f', 'r')):
        print("### Error: fingerprint('F00bar') is not ('a', 'b', 'f', 'r').")
        exit()

    if not isinstance(anagramish('Alberto', 'Bert'), bool):
        print("### Error: your definition of anagramish(w1, w2) doesn't return a Boolean.")
        exit()
    elif anagramish('Alberto', 'Bert'):
        print("### Error: anagramish('Alberto', 'Bert') returns True, False expected.")
        exit()
    elif not anagramish('Alberto', 'Bertalo'):
        print("### Error: anagramish('Alberto', 'Bertalo') returns False, True expected.")
        exit()
              
    if not isinstance(repeatIt('grain', 'ra'), str):
        print("### Error: your definition of repeatIt(S, target) doesn't return a string.")
        exit()
    if not repeatIt('grain', 'ra', 4) == 'grarararain':
        print("### Error: repeatIt('grain', 'ra', 4) does not return 'grarararain'.")
        exit()

    if not isinstance(squishIt('turnip', 'n'), str):
        print("### Error: your definition of squishIt(S, target) doesn't return a string.")
        exit()
    if not squishIt('turnip', 'n') == 'turip':
        print("### Error: your definition of squishIt('turnip', 'n') doesn't return 'turip'.")
        exit()

    print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
    exit()
