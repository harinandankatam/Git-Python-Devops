x=int(input('Enter min:'))
y=int(input('Enter max:'))
i=x
if i % 2 == 0 : i=x+1
while i<=y:
    print(i)
    i+=2
    