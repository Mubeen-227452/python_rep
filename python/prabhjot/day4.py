s = input("> ")
words = s.split(" ")
emoji = {
    ":)": "😊",
    ":(": "😂"
}
out = ""
for word in words:
    out += " " + emoji.get(word, word)
print(out)


def greet(name, age):
    print("hi " + name + " age is " + age)


d = input("enter user name: ")
a = input("enter user age: ")
greet(d, a)


class M:
    def wa(self):
        print("walk")


class D(M):
    pass


class C(M):
    pass


d1 = D()
print(d1.__name__)
d1.wa()

