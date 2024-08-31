my_list = [ 1, 2 , 9, 50, 100]

# squaredList = []

# for item in my_list:
#     squaredList.append(item*item)


# we can simplify these code using List Comphrension
squaredList = [i*i for i in my_list]

print(squaredList)