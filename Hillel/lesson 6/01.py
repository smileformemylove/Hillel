# b = int(input("Ввести сюда: "))
#
# a = 100
#
# a = True if b >= 100 else False
#
# print(a)

# a = 30
#
# b = []
#
# b_1 = [i ** 2 for i in range(12, a + 12)]
# print(b_1)

q = [1, 23, 54, 456, -5, 123]
q_new = [abs(i ** 3) for i in q]
print(q_new)