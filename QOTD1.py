# CS1210: QotD1
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
# Specification: range(lit, mpg) takes a number, lit, representing the
# numbers of liters of fuel left in your gas tank, and an integer,
# mpg, which is your (US model) car's fuel efficiency, expressed as
# miles per gallon, and returns your remaining driving range,
# expressed in kilometers.
#
# Example:
#   >>> range(10, 33)
#   140.18469656992085
#
# Hint: there are 3.79 liters per gallon, and 1.61 kilometers per
# mile.
#
# Note: your solution should be straightforward and concise; you
# should be able to solve this easily with a single statement.
#
# Hint: Replace the line that reads "pass" in the definition with 
# your own code.
#
def range(lit, mpg):
    return(lit / 3.79 * mpg * 1.61)

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
    if range(10, 33) is None:
        print("### Error: your definition of range(lit, mpg) doesn't return a value.")
    elif range(10, 33) <= 140.18 or range(10, 33) >= 140.19:
        print('### Error: range(10, 33) returns {}, expected ~140.185'.format(range(10, 33)))
    elif range(3.5, 38) <= 56.49 or range(3.5, 38) >= 56.5:
        print('### Error: range(3.5, 38) returns {}, expected ~56.5'.format(range(3.5, 38)))
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
