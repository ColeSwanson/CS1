# CS1210: QotD5
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the word "hawkid" between the two double quote marks to
# match your own hawkid. Your hawkid is the "login identifier" you use
# to login to all University services, like `https://myUI.uiowa.edu/'
#
# Note: we are not asking for your password, just the login
# identifier: for example, mine is "segre".
#
def signed():
    return(["ctswanson"])

######################################################################
# Specification: checkSequence(S, k) takes a string, S, and a
# nonnegative integer k such that k < len(S) and returns True if k is
# less than half the length of S and the kth element of S is less than
# the -kth element of S. In essence, you are comparing two elements of
# S that are equally distant from the two ends, returning True only
# when these are "in order."
#
# Example:
#   >>> checkSequence('alberto', 0)
#   True
#   >>> checkSequence('giovanni', 4)
#   False
#   >>> checkSequence([5, 4, 3, 2, 1], 1)
#   False
#
def checkSequence(S, k):
    Length = len(S)
    return(Length/2 > k and S[k] < S[Length-(k+1)])

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__':
    if type(signed()) is not list:
        print('### Error: Do not alter signed() other than to replace hawkid with your own.')
        exit()
    if signed()[0] == "hawkid":
        print('### Error: Replace the 6 characters in "hawkid" with your own hawkid in the signed() function.')
        exit()
    if checkSequence("student", 0) is None:
        print("### Error: your definition of checkSequence(S, k) doesn't return a value.")
    elif checkSequence("student", 0) != True:
        print("### Error: checkSequence('student', 0) returns {}, expected True".format(checkSequence("student", 0)))
    elif checkSequence("student", 1) != False:
        print("### Error: checkSequence('student', 1) returns {}, expected False".format(checkSequence("student", 1)))
    elif checkSequence(range(67891, 42, -13), 14) != False:
        print("### Error: checkSequence(range(67891, 42, -13), 14) returns {}, expected False".format(checkSequence(range(67891, 42, -13))))
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
