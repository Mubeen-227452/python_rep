file = open('data1.txt')
city = file.read().strip('""').split(",")

print('City Name:',city[2])
