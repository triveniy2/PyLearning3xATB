# List
#List Shopping list
# Milk, bread, butter, poha
# 1. Add items to the list
# 2. Remove items from the list
# 3. Print the list
# 4. view the list
# 5. Exit the program

shopping_list = ['Milk', 'bread', 'butter', 'poha']
print(shopping_list)
print(len(shopping_list))
print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
shopping_list.append("Curd")# add item at the end
print(shopping_list)
print(shopping_list[1])
shopping_list.insert(1,"Jam")
print(shopping_list[1])
print(shopping_list)
shopping_list.extend(["chips", "salt"])
print(shopping_list)
print(shopping_list.pop())
print(shopping_list)
print(shopping_list.index("butter"))
shopping_list[0]="triveni"
print(shopping_list)