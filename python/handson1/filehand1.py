
data = []
for line in open('dataforfilehand.txt'):
    item = []
    items = line.strip('\r\n').split('\n')   # strip new-line characters and split on column delimiter
    items = [item.strip() for item in items]  # strip extra whitespace off data items
    data.append(items)
print(data)
print(type(data))

for x in range(len(data)):
    print(data[x])

val = [("John", 102, 25000.00, 201, "Newyork"),("David",103,25000.00,202,"Port of spain"),("Nick",104,90000.00,201,"Newyork")]

print(val)
print(type(val))