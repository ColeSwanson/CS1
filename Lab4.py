# CS1210: Lab4 [3 functions to complete]
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
    return(["ctswanson","nengelthaler"])

######################################################################
# Specification: vPattern(S) takes a string, S, and returns a list of
# Booleans, where the ith element of the returned list is True if and
# only if S[i] is a vowel (here, we'll define a, e, i, o, and u to be
# the only vowels). Use a comprehension.
#
# Example:
#   >>> vPattern('dowel')
#   [False, True, False, True, False]
#   >>> vPattern("Alberto")
#   [True, False, False, True, False, False, True]
#
def vPattern(S):
    return[S.lower()[i] == "a" or S.lower()[i] == "e" or S.lower()[i] == "i" or S.lower()[i] == "o" or S.lower()[i] == "u" for i in range(len(S))]


######################################################################
# Specification: combine(I, S, T) takes an integer, I, a string, S,
# and a tuple, T, and returns a list containing all combinations of
# digits from I, characters from S, and elements from T.
#
# Example:
#   >>> combine(37, "am", ('x', 13))
#   [(3, 'a', 'x'), (3, 'a', 13), (3, 'm', 'x'), (3, 'm', 13), (7, 'a', 'x'), (7, 'a', 13), (7, 'm', 'x'), (7, 'm', 13)]
#
def combine(I, S, T):
    return[(int(i),s,t) for i in set(str(I)) for s in set(S) for t in set(T)]
######################################################################
# Specification: countEm(S, target) takes an string, S, and a target
# string, target, and returns a dictionary, where the keys are the
# elements of target and the values are the number of times that
# character appears in S. Here, case doesn't matter.
#
# Example:
#   >>> countEm('this is a test', 'txe')
#   {'t': 3, 'e': 1}
#   >>> countEm('Wild and woolly', 'Wolf')
#   {'w': 2, 'o': 2, 'l': 3}
#
def countEm(S, target):
    return{k:(S.lower().count(k)) for k in set(target.lower()) if S.lower().count(k)>0}

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__':
    if type(signed()) is not list:
        print('### Error: Do not alter signed() other than to replace hawkid with your own.')
        exit()
    if signed()[0][:min(len(signed()[0]),6)] == "hawkid"[:min(len(signed()[0]),6)]:
        print('### Error: Please update the signed() function to return your hawkids.')
        exit()

    if not isinstance(vPattern("foo"), list):
        print("### Error: your definition of vPatter(S) does not return a list.")
        exit()
    elif (vPattern('FoobAR') != [False, True, True, False, True, False]):
        print("### Error: vPattern('FoobAR') != [False, True, True, False, True, False]")
        exit()

    if not isinstance(combine(1, 'a', (2,)), list):
        print("### Error: your definition of combine(I,S,T) doesn't return a list.")
        exit()
    elif sorted(combine(13, 'ab', (0,))) != [(1, 'a', 0), (1, 'b', 0), (3, 'a', 0), (3, 'b', 0)]:
        print("### Error: sorted(combine(13, 'ab', (0,))) != [(1, 'a', 0), (1, 'b', 0), (3, 'a', 0), (3, 'b', 0)]")
        exit()
              
    if not isinstance(countEm('The rain in Spain', 'AIN'), dict):
        print("### Error: your definition of countEm(S, target) doesn't return a dictionary.")
        exit()
    if countEm('The rain in Spain', 'AIN') != {'a': 2, 'i': 3, 'n': 3}:
        print("### Error: countEm('The rain in Spain', 'AIN') != {'a': 2, 'i': 3, 'n': 3}")
        exit()

    print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
    exit()
