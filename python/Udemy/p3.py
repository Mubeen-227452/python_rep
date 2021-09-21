import random
import sys
import csv


class magic:
    def __init__(self, name):
        self.__name = name
        self.__mQuest = []
        self.__start_game()

    def __start_game(self):
        mResponse = ["IT IS CERTAIN", "YOU MAY RELY ON IT", "AS I SEE IT YES", "OUTLOOK LOOKS GOOD", "MOST LIKELY",
                     "IT IS DECIDEDLY SO", "WITHOUT A DOUBT", "YES DEFINITELY"]
        lQues = True

        print("welcome " + self.__name)

        while lQues:
            mQues = input("please enter ques: ")

            mRespond = mResponse[random.randint(0, 7)]

            if mQues == "":
                print("Thank you!")
                self.__wwrite_Ques()
                sys.exit()
            else:
                print(mRespond)
                self.__mQuest.append(mQues)
    def __wwrite_Ques(self):
        f=open("for8.csv","a",newline="")
        wrt=csv.writer(f)

        for q in self.__mQuest:
            wrt.writerow([q])

        f.close()
new8 = magic("mub")
