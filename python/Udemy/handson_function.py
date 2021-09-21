def get_word(word_type):
    if word_type.lower() == 'adjective':
        a_or_an = 'an'
    else:
        a_or_an = 'a'
    return input('Enter a word that is {0} {1}:'.format(a_or_an, word_type))


def fill(noun, verb, adjective):
    story = "In this course you will learn how to {1}." \
            "it's so easy even a {0} can do it." \
            "trust me, it will be very {2}.".format(noun, verb, adjective)
    return story


def display(story):
    print()
    print('here is story')
    print()
    print(story)


def c_story():
    noun = get_word('noun')
    verb = get_word('verb')
    adj = get_word('adjective')
    the_s = fill(noun, verb, adj)
    display(the_s)


c_story()
