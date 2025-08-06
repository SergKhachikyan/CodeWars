my_list = [-3,-2,0,1]

for i in range(len(my_list)):
    if my_list[i] - my_list[i - 1] == 2:
        print(my_list[i])
        break
else:
    print("None")