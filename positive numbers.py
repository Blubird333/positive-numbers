list1 = []
i1 = int(input("enter the first number:"))
i2 = int(input("enter the second number:"))
i3 = int(input("enter the third number:"))
i4 = int(input("enter the fourth number:"))
i5 = int(input("enter the fifth number:"))
list1.append(i1)
list1.append(i2)
list1.append(i3)
list1.append(i4)
list1.append(i5)
list2 = []
for i in list1:
    if i>0:
     list2.append(i)
     i = i+1
print("The positive numbers are:",list2)     
