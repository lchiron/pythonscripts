mylist = [2, 3, 1, 222, 4, 11, 22, 5]

#外层表示循环多少论
for i in range(len(mylist)-1):
    #内层循环每轮两两比较多少次
    for j in range(len(mylist)-1-i):

        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)