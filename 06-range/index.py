#  起始点 终止点 步长
# a = range(1,10,2)

# print(a , list(a))


count = 0

point = 0

while point < 100:
    if point % 2 == 0:
        # is odd
        count += point
    point += 1

print(count)