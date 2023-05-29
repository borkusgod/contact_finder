# main for ./honeyz_proj/contact_finder

var_tester = "abcdefg"
var_tester2 = "abc4defg"

def stepper(incoming):
    for each in incoming:
        print(type(each))
        print(each)
        check = each.isdigit()
        if check:
            print('This is a number')

stepper(var_tester)
print('\n')
stepper(var_tester2)