def cat_say(text):
    text_length = len(text)
    print('         {}'.format('_' * text_length))
    print('        <{}>'.format(text))
    print('         {}'.format('-' * text_length))
    print('       /')
    print('/\_/\ /')
    print('(o.o)')
    print('>~<')


def main():
    text = input('What would u like:? ')
    cat_say(text)


if __name__ == '__main__':
    main()
