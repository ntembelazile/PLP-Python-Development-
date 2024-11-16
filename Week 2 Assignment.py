# creatng an empty List[]
my_list = []

#adding values to an empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting value using index position
my_list.insert(1,15)

#create new_list[]
new_list = [50,60,70]

#extend my_list[] with new_list[]
my_list.extend(new_list)

#remove the last element from a list
my_list.pop()

#sorting my_list in ascending order by default
my_list.sort()

#print the index of the value 30 in my_list
print(my_list.index(30))

print(my_list)