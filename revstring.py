s = str(input('Enter sentaince:'))
x = s.split()
print (x)
result = []
i = 0
while i <len(x):
    result.append(x[i][::-1])
    i=i+1
print (result) 
output = ' ' .join(result)
print (output)   
#y = (x[0][::-1])
#print(y)