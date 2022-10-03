# CS1210: QotD6
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
# Specification: extendListByMinMaxElements(L) takes a list, L, of
# nonnegative integers and modifies L by removing its smallest element
# and then adding that number of copies of the largest element of L to
# the end of L. The function should not return a value (i.e., it
# returns None), having, however, modified L.
#
# Example:
#
# Note how only the first copy of the smallest element is removed at
# each invocation. You will want to brush up on your list methods from
# [PE] 8.6-8.7.
#
def extendListByMinMaxElements(L):
    minnimum = min(L)
    maximum = max(L)
    L.remove(minnimum)
    for i in range(minnimum):
        L.append(maximum)
    pass

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
    # Careful! Because function changes L, these tests must be run
    # from the following value of L in exactly this sequence.
    L = [4, 1, 0, 7, 3, 0]
    if extendListByMinMaxElements(L) is not None:
        print("### Error: your definition of extendListByMinMaxElements(L) doesn't return None.")
    elif extendListByMinMaxElements(L) is None and L!=[4, 1, 7, 3]:
        print("### Error: expecting [4, 1, 7, 3] when L is [4, 1, 7, 3, 0]");
    elif extendListByMinMaxElements(L) is None and L!=[4, 7, 3, 7]:
        print("### Error: expecting [4, 7, 3, 7] when L is [4, 1, 7, 3]");
    elif extendListByMinMaxElements(L) is None and L!=[4, 7, 7, 7, 7, 7]:
        print("### Error: expecting [4, 7, 7, 7, 7, 7] when L is [4, 7, 3, 7]");
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
