import sys
import random

res = ["IT IS CERTAIN", "YOU MAY RELY ON IT", "AS I SEE IT YES", "OUTLOOK LOOKS GOOD", "MOST LIKELY",
       "IT IS DECIDEDLY SO", "WITHOUT A DOUBT", "YES DEFINITELY"]
q = True
while q:
    ques = input("please enter the 8 ball question ")
    if ques == "":
        sys.exit()
    else:
        print(res[random.randint(0, 7)])
