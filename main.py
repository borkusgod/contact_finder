# main for ./honeyz_proj/contact_finder
import re

var_tester = "abcdefg"
var_tester2 = "abc4defg"

# regex test lists
testing_str = [
    "one",
    "two",
    "three",
    "etc"
]

non_link_str = "https://www.blahblah.com"
link_str = "https://info@myemail.com"

def stepper(incoming):
    for each in incoming:
        print(type(each))
        print(each)
        check = each.isdigit()
        if check:
            print('This is a number')

def chk4email(incoming):
    at_found = False
    for each in incoming:
        if each == "@":
            at_found = True
    return at_found

non = chk4email(non_link_str)
link = chk4email(link_str)

if non is True:
    print(f"{non_link_str} is an email address")
else:
    print(f"{non_link_str} is not an email address")

if link is True:
    print(f"{link_str} is an email address")
else:
    print(f"{link_str} is not an email address")
        

#stepper(var_tester)
#print('\n')
#stepper(var_tester2)
