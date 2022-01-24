import sys

lst = sys.argv
acc=10000
if lst[1] == '1':
    print ('Account Balance:', acc)
elif lst[1] == '2':
    acc1 = int(input('Enter amount to deposit:'))
    acc = acc+acc1
    print(acc)
elif lst[1] == '3':
    acc2 = int(input('Enter amount to withdraw:'))
    acc = acc-acc2
    print(acc)
    