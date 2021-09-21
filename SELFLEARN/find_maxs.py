from maxfun import find_max

number=[]
n=int(input("enter the no of elements>:"))
print(f"enter the {n} values")
for i in range(0,n):
    values=int(input(">"))
    number.append(values)

maximum=find_max(number)
print(f'The maximum value is :{maximum}')