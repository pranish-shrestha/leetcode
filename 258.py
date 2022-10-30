def addDigits(num: int) -> int:
    while num > 9:
        sum = 0
        for n in str(num):
            sum += int(n)
        num = sum
    return num

print(addDigits(num = 0))