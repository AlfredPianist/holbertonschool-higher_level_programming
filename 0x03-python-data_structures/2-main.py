#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]

print("Original list")
print(my_list)

idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print("New list with idx 3 replaced by 9")
print(new_list)
print(my_list)

new_list = replace_in_list(my_list, -2, 5)
print("New list with idx -2 replaced by 5")
print(new_list)
print(my_list)

new_list = replace_in_list(my_list, 5, 20)
print("New list with idx 5 replaced by 20")
print(new_list)
print(my_list)

new_list = replace_in_list(my_list, 4, 20)
print("New list with idx 4 replaced by 20")
print(new_list)
print(my_list)
