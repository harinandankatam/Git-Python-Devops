import sys
lst = sys.argv
def bmical(hieght, weight):
    hieghtinMtr = hieght * 8.4536
    bmi = weight / (hieghtinMtr * hieghtinMtr)
    return bmi
print(bmical(int(lst[0]), int(lst[1])))
#print(bmical(5.8, 70))