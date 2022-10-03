# CS1210: QotD10
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
# Specification: countVowels(S, vowels='aeiou') takes a string, S,
# consisting of multiple words, and a collection of vowels
# (characters) and returns a dictionary where the keys are lower-cased
# words in S and the values are themselves dictionaries with the keys
# being the vowels and the values being the number of times that vowel
# appears in the particular word. An example should help make this
# clear.
#
# Example:
#   >>> countVowels("Won't you please let me back in your heart?")
#   {"won't": {'o': 1}, 'you': {'o': 1, 'u': 1}, 'please': {'a': 1, 'e': 2}, 'let': {'e': 1}, 'me': {'e': 1},
#    'back': {'a': 1}, 'in': {'i': 1}, 'your': {'o': 1, 'u': 1}, 'heart?': {'a': 1, 'e': 1}}
#
# Your solution should use only comprehensions, and not some other
# form of iteration. As always, concise solutions without unnecessary
# steps or structures are preferred.
#
def countVowels(S, vowels='aeiou'):
    return{word.lower():{v:word.lower().count(v) for v in set(vowels) if word.lower().count(v) > 0} for word in S.split()}
######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__':
    if type(signed()) is not list:
        print('### Error: Do not alter signed() other than to replace hawkid with your own.')
        exit()
    if signed()[0][:min(len(signed()[0]),6)] == "hawkid"[:min(len(signed()[0]),6)]:
        print('### Error: Please update the signed() function to return your hawkid.')
        exit()
    if not isinstance(countVowels('Let me tell ya now', 'a'), dict):
        print("### Error: your definition of countVowels(S, vowels) does not return a dict.")
    elif countVowels('Let me tell ya now') != {'let': {'e': 1}, 'me': {'e': 1}, 'tell': {'e': 1}, 'ya': {'a': 1}, 'now': {'o': 1}}:
        print("### Error: expecting countVowels('Let me tell ya now') to return {'let': {'e': 1}, 'me': {'e': 1}, 'tell': {'e': 1}, 'ya': {'a': 1}, 'now': {'o': 1}}")
        exit
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
        exit()
