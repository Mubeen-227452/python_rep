file = open("ex.txt", "r")
for x in file:
    title=x.split()
    for a in title:
        print(a[0],end='')
    print()

file.close()

print("hi iam")