n = int(input("Enter a number: "))
p = 0
m = 0
for i in range(10):
                  m = m+1
                  p = n*m
                  print(n,"x",m, "=", p)
i = int(input("Enter a value for i: "))
j = int(input("Enter a value for j: "))
while j<=i:
         j = int(input("Enter a value for j: "))
while i<=j:
          p = n*i
          print(n,"x",i, "=",p)
          i = i+1 
