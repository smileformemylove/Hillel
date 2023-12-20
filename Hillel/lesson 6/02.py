def summa(a, b):
    result = a + b
    result += 1
    result /= 3
    result = round(result)
    return result


a = 10
b = 20
c = summa(a, b)
print(c)