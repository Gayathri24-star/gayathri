array1=[1,2,3,4,5]
array2=[4,5,6,7,8]
common_values=set(array1).intersection(set(array2))
common_values=list(common_values)
print("Common values between the two arrays:",common_values)
