# CS1210: QotD7
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
# Specification: meiosis(L1, L2, k, j) takes two lists, L1 and L2, and
# two integers, k and j such that both are valid indexes in both x and
# y, and modifies both L1 and L2 by swapping subsections of each list
# between k and j (or more precisely, j-1). The function returns no
# value.
#
# Example:
#   >>> x=[0, 1, 2, 3, 4, 5]
#   >>> y=list('abcdefgh')
#   >>> meiosis(x, y, 2, 4)
#   >>> x
#   [0, 1, 'c', 'd', 4, 5]
#   >>> y
#   ['a', 'b', 2, 3, 'e', 'f', 'g', 'h']
#
# Why meiosis? Your friend the biology major can explain, or look it
# up.
#
# Note: You will need assignment, but you don't need conditionals,
# iteration, or any other such construct. Solutions that use
# extraneous constructs will not receive credit. This is a simple
# one-liner.
#
def meiosis(L1, L2, k, j):
    temp = L1[k:j]
    L1[k:j] = L2[k:j]
    L2[k:j] = temp
    return

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
    # Careful! Because function changes x and y, these tests must be
    # run from the following value of x and y in exactly this
    # sequence.
    x = list(range(3, 15, 2))
    y = list(range(8, 20, 2))
    print("### Note: x is initially [3, 5, 7, 9, 11, 13]")
    print("### Note: y is initially [8, 10, 12, 14, 16, 18]")
    if meiosis(x, y, 0, 0) is not None:
        print("### Error: your definition of meiosis(L1, L2, k, j) doesn't return None.")
    elif not (meiosis(x, y, 2, 4) is None and x==[3, 5, 12, 14, 11, 13] and y==[8, 10, 7, 9, 16, 18]):
        print("### Error: expecting meiosis(x, y, 2, 4) to leave x==[3, 5, 12, 14, 11, 13] and y==[8, 10, 7, 9, 16, 18]")
        exit
    elif not (meiosis(x, y, -3, -1) is None and x==[3, 5, 12, 9, 16, 13] and y==[8, 10, 7, 14, 11, 18]):
        print("### Error: expecting meiosis(x, y, -3, -1) to leave x==[3, 5, 12, 9, 16, 13] and y==[8, 10, 7, 14, 11, 18]")
        exit
    elif not (meiosis(x, y, -2, max(len(x), len(y))) is None and x==[3, 5, 12, 9, 11, 18] and y==[8, 10, 7, 14, 16, 13]):
        print("### Error: expecting meiosis(x, y, -2, max(len(x), len(y))) to leave x==[3, 5, 12, 9, 11, 18] and y==[8, 10, 7, 14, 16, 13]")
        exit
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
