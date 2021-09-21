command=''
start=False
while command != "quit":
    command=input("> ").lower()
    if command=='start':
        if start:
            print("car already started")
        else:
            start=True
            print("car started....")
    elif command=='stop':
        if not start:
            print("car already stopped")
        else:
            start=False
            print("car stopped...")
    elif command =='help':
        print('''
        Start-start the car
        stop-stop the car
        quit-to quit''')
    elif command=='quit':
        break
else:
    print('sorry im not understand')