# Random list with its sort
# import random
# a = 0
# t = []
# while a < 10:
#     t.append(random.randint(1, 100))
#     a += 1
# print(t)
# a = 0
# while a < len(t) - 1:
#     b = 0
#     while b < len(t) - 1:
#         if t[b] > t[b + 1]:
#             c = t[b]
#             t[b] = t[b + 1]
#             t[b + 1] = c
#         b += 1
#     a += 1
# print(t)

# import random
# t = [[], [], []]
# a = 0
# while a < 3:
#     b = 0
#     while b < 3:
#         t[a].append(bool(random.randint(0, 1)))
#         b += 1
#     a += 1
# print(t)

# import random
# t = [[], [], [], [], []]
# c = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
# a = 0
# while a < 5:
#     b = 0
#     while b < 5:
#         t[a].append(random.randint(0, 9))
#         b +=1
#     a += 1
# a = 0
# while a < 5:
#     print(c[t[a][0]], c[t[a][1]], c[t[a][2]], c[t[a][3]], c[t[a][4]])
#     a += 1

# from progressbar import ProgressBar
# import time
# bar = ProgressBar(maxval = 10)
# bar.start()
# time.sleep(2)
# bar.update(5)
# time.sleep(2)
# bar.update(10)
# time.sleep(2)
# bar.finish()

# https://stackoverflow.com/questions/3160699/python-progress-bar
# from alive_progress import alive_bar; import time
# for total in 5000, 7000, 4000, 0:
#     with alive_bar(total) as bar:
#         for _ in range(5000):
#             time.sleep(.001)
#             bar()

# from progressbar import ProgressBar; import time
# print('I have to send a error report')
# a = 0
# bar = ProgressBar(maxval = 100)
# bar.start()
# while a < 100:
#     time.sleep(0.01)
#     bar.update(a)
#     a += 0.5
# bar.finish()
# print('Report sent')

# from progressbar import ProgressBar; import random
# points = 0
# bar = ProgressBar(maxval = 6)
# bar.start()
# a = 0
# while a < 6:
#     b = random.randint(1, 20)
#     c = random.randint(1, 20)
#     answer = int(input(str(b) + ' + ' + str(c) + ' = '))
#     if b + c == answer:
#         points += 1
#     bar.update(points)
#     a += 1

