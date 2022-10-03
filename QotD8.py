# CS1210: QotD8
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
# Specification: smooshOdds(n) takes a nonnegative integer, n, and
# returns a new integer consisting only of the odd digits in n.
#
# Example:
#   >>> smooshOdds(19054249)
#   1959
#
# Your solution should make use of a comprehension.
#
def smooshOdds(n):
    if (''.join([str(integer) for integer in [int(i) for i in str(n)] if integer%2 == 1])) == '':
        solve = None #return None if there are no odd characters in integer because there is no integer to return
    else:
        solve = int(''.join([str(integer) for integer in [int(i) for i in str(n)] if integer%2 == 1]))
    return(solve)

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
    if type(smooshOdds(12319)) is not int:
        print("### Error: your definition of smooshOdds(n) does not return an int.")
    elif smooshOdds(12319) != 1319:
        print("### Error: expecting smooshOdds(12319) to return 1319")
        exit
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
