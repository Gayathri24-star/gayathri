import array

my_list = [1, 2, 3, 4, 5]
array_from_list = array.array('i', my_list)

my_tuple = (6, 7, 8, 9, 10)
array_from_tuple = array.array('i', my_tuple)

print("Array from list:", array_from_list)
print("Array from tuple:", array_from_tuple)
