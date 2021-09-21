bill = [['bill001', 1, 'item001', 35.00, 33.00, 'wt.', 5.00],
        ['bill001', 2, 'item021', 350.00, 330.00, 'nos', 1.00],
        ['bill058', 1, 'item401', 150.00, 145.00, 'ltr', 5.00],
        ['bill121', 1, 'item001', 35.00, 33.00, 'wt.', 5.00],
        ['bill121', 2, 'item021', 350.00, 330.00, 'nos', 1.00],
        ['bill121', 3, 'item401', 150.00, 145.00, 'ltr', 5.00]
        ]

print(bill[0])


def unique(list1):
    new_list = []
    for x in range(len(list1)):
        new_list.append(bill[x][0])
    return new_list


new_bill =set(unique(bill))
print(new_bill)
new_bill.add('bill121')
print(new_bill)
new_bill.add('bill059')
print(new_bill)