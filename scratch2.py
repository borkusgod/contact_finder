word = "found"

string_tester = "ifoundawordinasentence"

# if word in string_tester:
#     print('word found')

test_list1 = [1, 2, 3]
test_list2 = [1, 2, 3, 4, 5]
test_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def get_whl(number):
    from_arg = number
    to_whole = int(from_arg)
    back_to_float = float(to_whole)
    return from_arg - back_to_float


perc_of1 = float(len(test_list1)) * 0.75
print(perc_of1)
left_over = get_whl(perc_of1)
if left_over >= .5:
    print('round up')
else:
    print('round down')
print(left_over)

print('\n')

perc_of2 = float(len(test_list2)) * 0.75
print(perc_of2)
left_over = get_whl(perc_of2)
if left_over >= .5:
    print('round up')
else:
    print('round down')
print(left_over)

print('\n')

perc_of3 = float(len(test_list3)) * 0.75
print(perc_of3)
left_over = get_whl(perc_of3)
if left_over >= .5:
    print('round up')
else:
    print('round down')
print(left_over)

first_list = [1, 2, 3]
second_list = [4, 5, 6]
third_list = [7, 8, 9]
list_container = []

list_container.append(first_list)
list_container.append(second_list)
list_container.append(third_list)
print(list_container)
