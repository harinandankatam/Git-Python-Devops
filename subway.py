print('Toppings: \n onions \n tomato \n Lettuce \n Olives \n Pepper')
s=[x for x in input('Pick your Toppings:').split()]
h=int(input('How many Burgers:'))
p=50
print('your Toppings:',s)
print('Total bill:',h*p)