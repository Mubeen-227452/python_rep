n=int(input("Enter the number of names:\n"))
l=[]
z=[]
if n>0:
    print("Enter the names:")
    for i in range(n):
        l.append(input())
    print("The sorted name list is:")
    print(l.sort(key=len,reverse=True))
else:
    print("Invalid")