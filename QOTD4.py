# CS1210: QotD4
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
# Specification: wedge(S, i, j, U) takes two strings, S and U, and two
# integers 0 <= i,j < len(S), and returns a news string that replaces
# elements i through j-1 of S with U.
#
# Example:
#   >>> wedge('abcdefg', 2, 4, 'FOO')
#   'abFOOefg'
#   >>> wedge('abcdefg', 0, 1, 'FOO')
#   'FOObcdefg'
#   >>> wedge('abcdefg', 0, 0, 'FOO')
#   'FOOabcdefg'
#   >>> wedge('abcdefg', 5, 3, 'FOO')
#   'abcdeFOOdefg'
#
def wedge(S, i, j, U):
    NewBeginning = S[:i]
    NewEnd = S[j:]
    return(NewBeginning + U + NewEnd)

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
    if wedge("student", 3, 2, ' ') is None:
        print("### Error: your definition of wedge(S, i, j, U) doesn't return a value.")
    elif wedge("student", 3, 6, 'CS1210') != 'stuCS1210t':
        print("### Error: wedge('student', 3, 5, 'CS1210') returns {}, expected ''".format(wedge("student", 3, 5, 'CS1210')))
    elif wedge("student", 3, 2, ' ') != 'stu udent':
        print("### Error: wedge('student', 3, 2, ' ') returns {}, expected ''".format(wedge("student", 3, 2, ' ')))
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
