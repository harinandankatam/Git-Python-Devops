m=int(input('Enter marks for Maths:'))
p=int(input('Enter marks for Physics:'))
c=int(input('Enter marks for Chemistry:'))
#avg=m++p+c/3
if (m+p+c>=105):
    avg=int((m+p+c)/3)
    print('Average:',avg)
    if(avg>=90):
        print("Grade: A")
    elif(avg>=80&avg<90):
        print("Grade: B")
    elif(avg>=70&avg<80):
        print("Grade: C")
    elif(avg>=60&avg<70):
        print("Grade: D")
    else:
        print("Grade: F") 
    
else:
    print("Failed")
    
    
    
    
    
    
    
    
    
    
