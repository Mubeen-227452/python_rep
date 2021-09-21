def find_max(numbers):
    maX = numbers[0]
    for num in numbers:
        if num > maX:
            maX = num
    return maX
