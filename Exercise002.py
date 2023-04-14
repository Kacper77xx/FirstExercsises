# list = ['a', 'b', 'c', 'd']
# for i in range(0, len(list)):
#     print(list[i])
#     if list[i] == 'b':
#         # print('Beata')

# import random
# a = 3
# b = int(3*a)
# print(random.randint(a, b))

# import random
# amount = random.randint(1, 15)
# text = 'cookie'
# print(amount*text)

import random
import time
points = 0
while True:
    n1 = random.randint(0, 101)
    n2 = random.randint(0, 101)
    print('n1 =',n1)
    print('n2 =',n2)
    difference = n1 - n2
    t1 = time.time()
    print('n1 - n2 = ?')
    print('Give me a result!')
    user = int(input())
    if difference == user:
        print('Correct!')
        t2 = time.time()
        t3 = t2 - t1
        points += 1
        print('You needed ' + str(round(t3, 2)) + ' seconds for this')
    else:
        print('Wrong!')
        points -= 1
    print('n1 - n2 = ' + str(difference))
    print('Your streak: ' + str(points))
    continue
