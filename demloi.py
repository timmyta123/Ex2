string = str( input ("Hay nhap gi do:"))
A=string.split()
count=0
sai=0
for a in A:
    if  a[0].isupper() == True:
        count=count +1
    else :
        sai= sai+1
print("So tu dung la:",count)
print("So tu sai la:",sai)