l1=eval(input('Enter values:'))
print(l1)
l2=[]
for each_value in l1:
    if each_value not in l2:
       l2.append(each_value)
print(l2)