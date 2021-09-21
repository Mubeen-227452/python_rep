bill = ['bill001', 1, 'item001', 35.00, 33.00, 'wt.', 5.00]


def swapPositions(ex, pos1, pos2):
    ex[pos1], ex[pos2] = ex[pos2], ex[pos1]
    return ex


print(bill)
print(type(bill))
print(dir(bill))
d = sorted([str(x) for x in bill])
print(d)
print(swapPositions(bill, 5, 6))
bill.insert(0, '17/06/2021')
print(bill)
