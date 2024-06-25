def getJieCheng(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


print("getJieCheng 3:", getJieCheng(3))
print("getJieCheng 6:", getJieCheng(6))
print("getJieCheng 100:", getJieCheng(100))
