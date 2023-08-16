n = int(input("Enter a number: "))  
while n<1:
         n = int(input("Enter a number ")) 
if n==2:
       print("prime")
else:   
    i = 1
    while i<n-1:
               i=i+1
               if n%i==0:
                 break                     
    if n%i==0 or n==1:
                     print("composite")
    else:                   
        print("prime")
                                      
