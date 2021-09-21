"""n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l." + cmd)
    else:
        print(l)
"""
phone=input("enter ph number:> ")
digit_map={"1":"one","2":"two","3":"Three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
op=''
for ch in phone:
    op+=digit_map.get(ch,"!")+" "
print(op)