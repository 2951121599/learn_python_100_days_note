# s = '1'
# print(type(s))

# s = int(s)
# print(type(s))

# f = int(input('tip:'))
# print(f)

# year = int(input('请输入年份: '))
# # 如果代码太长写成一行不便于阅读 可以使用\或()折行
# is_leap = (year % 4 == 0 and year % 100 != 0 or
# year % 400 == 0)
# print(is_leap)

# if condition:
#     pass
# elif condition:
#     pass
# else:
#     pass


# for i in range(1, 10):  # 1  2  3  4  5  6  7  8  9
#     for j in range(1, i+1):  # 1
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('%d, %s' % (x, y))

# from random import randint
# face = randint(0, 6)
# print(face)


# import time
# print(time.time())


sum = 0
for x in range(1, 10, 2):
    print(x)
    # sum = sum + x
# print(sum)


from day02 import add

print(add(3,4,5))