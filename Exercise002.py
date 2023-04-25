# list = ['a', 'b', 'c', 'd']
# for i in range(0, len(list)):
#     print(list[i])
#     if list[i] == 'b':
#         # print('Beata')
import random

# import random
# a = 3
# b = int(3*a)
# print(random.randint(a, b))

# import random
# amount = random.randint(1, 15)
# text = 'cookie'
# print(amount*text)

# import random
# import time
# points = 0
# while True:
#     n1 = random.randint(0, 101)
#     n2 = random.randint(0, 101)
#     print('n1 =',n1)
#     print('n2 =',n2)
#     difference = n1 - n2
#     t1 = time.time()
#     print('n1 - n2 = ?')
#     print('Give me a result!')
#     user = int(input())
#     if difference == user:
#         print('Correct!')
#         t2 = time.time()
#         t3 = t2 - t1
#         points += 1
#         print('You needed ' + str(round(t3, 2)) + ' seconds for this')
#     else:
#         print('Wrong!')
#         points -= 1
#     print('n1 - n2 = ' + str(difference))
#     print('Your streak: ' + str(points))
#     continue

# t = ['Dog', 'Cat', 'Horse', 'Turtle']
# print(t)
# a = 0
# while a < 4:
#     print(t[a])
#     a += 1

# import random
# numbers = [random.randint(1, 80), random.randint(1, 80), random.randint(1, 80)]
# a = 0
# while a < 3:
#     print(numbers[a])
#     a += 1

# t = [7]
# t.append(10)
# print(len(t))

# import random
# t = [random.randint(1, 10)]
# while t[len(t) - 1] != 7:
#     t.append(random.randint(1, 10))
#     a = 0
#     while a < len(t):
#         print(t[a])
#         a += 1

# print('Tell me your favorites movies!')
# movies = []
# userMovies = ''
# while userMovies != 'End':
#     userMovies = input()
#     if userMovies != 'End':
#         movies.append(userMovies)
# a = 0
# while a < len(movies):
#     print(movies[a])
#     a += 1

# import random
# t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(t)
# print(t)

import random
number = random.randint(1, 10)
a = 1
t5 = []
while a < 6:
    t5.append(a * number)
    a += 1
random.shuffle(t5)
print(t5[0], t5[1], t5[2], t5[3])
print('Write a last number!')
userAns = int(input())
if userAns == t5[4]:
    print('Correct!')
else:
    print('Incorrect')
    print('Right answer is ' + str(t5[4]))