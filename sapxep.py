import array
string = str( input ("Hay nhap gi do:"))
A=string.split()
dup = int(0)
count = int(0)
out = str()
print (A)
for a in A:
    for b in A:
        if a == b :
            dup += 1
            if dup > 1:
                A[count]=""
    count+= 1
    dup = 0
A.remove("")
A.sort()
for x in A:
    out = out + x + " "
print(out)


