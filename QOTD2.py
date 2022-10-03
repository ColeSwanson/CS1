# CS1210: QotD2
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
    return(["Ctswanson"])

######################################################################
# Specification: jujitsu(S, k) takes a sequence, S, and an integer, k,
# and returns a new sequence containing the kth through the last
# elements of S followed by the first k elements of S in reverse
# order.
#
# Example:
#   >>> jujitsu((1, 2, 3, 4, 5, 6, 7), 2)
#   (3, 4, 5, 6, 7, 2, 1)
#   >>> jujitsu("abcdefgh", 5)
#   'fghedcba'
#
# Note that if k > len(S), the result should just be the sequence S in
# reverse order.
#
# Note: your solution should be straightforward and concise; you
# should be able to solve this easily with a single statement.
#
# Hint: Replace the line that reads "pass" in the definition with 
# your own code.
#
def jujitsu(S, k):
    NewBeginning = S[k:]
    ReversedString = S[::-1]
    NewEnd = ""
    if(k!=0):
        NewEnd = ReversedString[-k:]
    return(NewBeginning + NewEnd)

        

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
    if jujitsu("student", 3) is None:
        print("### Error: your definition of jujitsu(S, k) doesn't return a value.")
    elif jujitsu("student", 0) != 'student':
        print("### Error: jujitsu('student', 0) returns {}, expected 'student'".format(jujitsu("student", 0)))
    elif jujitsu("student", 3) != 'dentuts':
        print("### Error: jujitsu('student', 3) returns {}, expected 'dentuts'".format(jujitsu("student", 3)))
    elif jujitsu("student", 1) != 'tudents':
        print("### Error: jujitsu('student', 1) returns {}, expected 'tudents'".format(jujitsu("student", 1)))
    elif jujitsu((1, 2, 3, 4), 2) != (3, 4, 2, 1):
        print("### Error: jujitsu((1, 2, 3, 4), 2) returns {}, expected (3, 4, 2, 1)".format(jujitsu((1, 2, 3, 4), 2)))
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
