def time_to_seconds(hours,minutes):
    print(hours * 60 * 60 + minutes * 60)

time_to_seconds(1,50)
print([s.upper() for s in ['hello', 'world']])

def add_many(*args):
    s = 0
    for n in args:
        s += n
    print(s)

add_many(100, 50, 3)


class Planet:
    def __init__(self, name, diameter_km):
        self.name = name
        self.diameter_km = diameter_km


e =Planet('Earth',12742)

print(e.name, e.diameter_km)

def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

print(factorial.__doc__)

print([i *2 for i in range(5)])
M = [x for x in range(5) if x >2]
print(M)
def square(x):
    'Returns the square of the argument x'

    return x * x

print(square.__doc__)
print([i * 3 for i in range(5)])

s = "fox"

print(s.format(4))
print(s.rjust(4))

class AstroBody:
    description = 'Natural entity in the observable universe.'

class Star(AstroBody):
    pass

sun = Star()

print(sun.description)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.intersection(b))
"""import random
random.seed(2427)

def efficient_sample(n):
  x = [write code here for write code here]
  return x

efficient_sample(20)"""
w = 'python'

w_iterator = iter(w)

print(next(w_iterator))


def count_words(filename):
    """Count the number of words in a file"""
    try :
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except  FileNotFoundError:
        print("The file {} cannot be found".format(filename))
    else:
        words = contents.split()
        num_words = len(words)
        print("The file {} has about {} words.".format(filename, num_words))

filename = "peter_rabbit.txt"
count_words(filename)