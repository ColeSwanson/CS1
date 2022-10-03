# CS1210: QotD3
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
# Specification: center(S, k) takes a sequence, S, and a nonnegative
# integer, k, and returns a new sequence consisting of only the
# "center k" elements of S.
#
# Example:
#   >>> center((1, 2, 3, 4, 5, 6, 7), 2)
#   (3, 4)
#   >>> center("abcdefgh", 3)
#   'cde'
#   >>> center("abcdefgh", 4)
#   'cdef'
#   >>> center("abcdefgh", 5)
#   'bcdef'
#
# Note that if k >= len(S), the result should just be the sequence S.
# Note also that if len(S) is even but k is odd (or vice versa) the
# solutions is a bit skewed to the left; this is clear from the
# examples above.
#
def center(S, k):
    Length = len(S)
    n = (Length-k)//2
    o = (Length-k)%2
    Solution = S[n:-(n+o)]
    return(Solution)

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
    if center("student", 3) is None:
        print("### Error: your definition of center(S, k) doesn't return a value.")
    elif center("student", 0) != '':
        print("### Error: center('student', 0) returns {}, expected ''".format(center("student", 0)))
    elif center("student", 3) != 'ude':
        print("### Error: center('student', 3) returns {}, expected 'ude'".format(center("student", 3)))
    elif center("student", 1) != 'd':
        print("### Error: center('student', 1) returns {}, expected 'd'".format(center("student", 1)))
    elif center((1, 2, 3, 4), 2) != (2, 3):
        print("### Error: center((1, 2, 3, 4), 2) returns {}, expected (2, 3)".format(center((1, 2, 3, 4), 2)))
    elif center((1, 2, 3, 4), 1) != (2,):
        print("### Error: center((1, 2, 3, 4), 1) returns {}, expected (2,)".format(center((1, 2, 3, 4), 1)))
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
