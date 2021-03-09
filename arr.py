import array
n= int(input("Hay nhap so phan tu cua mang:"))
m= 1
A= []
count=0
while m <= n :
    w =int (input ("Hay nhap mot so:"))
    A.append(w)
    m= m+1

for x in A :
   if x < 0 :
        A[count] = 0

   elif x == 2:
       print("So nguyen to chan la 2")
   count += 1

print(A)
