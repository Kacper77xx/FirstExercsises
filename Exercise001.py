# import time
# wday = time.gmtime()
# if wday[6] < 4:
#     print('Just give me Friday!')
# elif wday[6] == 4:
#     print('Finally it is Friday!')

# import time
# print('Guess the amount of seconds game!')
# print()
# print('You will have three seconds wait to start, get ready!')
# # time.sleep(3)
# currentSec = time.gmtime()
# userSec = int(input("Give me a seconds which appear on Windows's clock: "))
# if userSec == currentSec[5]:
#     print('Congrats! Perfect shoot!')
# else:
#     print("Unlucky, you've to repeat!")
# print('Correct answer is: ', time.strftime('%S', time.gmtime()))
# points = 0
# print('First question:')
# print('2 + 2 = ?')
# q1 = int(input())
# if q1 == 4:
#     print(str(int(True)) + ' point')
#     points += 1
# else:
#     print(int(False))
# print('Second question:')
# print('Language of England is...?')
# q2 =input()
# if q2 == 'English':
#     print(str(int(True)) + ' point')
#     points += 1
# elif q2 == 'english':
#     print(str(int(True)) + ' point')
#     points += 1
# else:
#     print(int(False))
# print('Third question:')
# print("What animal do 'How how'?")
# q3 = input()
# if q3 == 'Dog':
#     print(str(int(True)) + ' point')
#     points += 1
# elif q3 == 'dog':
#     print(str(int(True)) + ' point')
#     points += 1
# else:
#     print(int(False))
# print('You received: ' + str(points))
import random
n1 = random.randint(1, 101)
n2 = random.randint(1, 101)
n3 = random.randint(1, 101)
print(str(n1) + ' ' + str(n2) + ' ' + str(n3))
userChoice = int(input('Choose the highest number! '))
if userChoice == n1:
    if n1 > n2:
        if n1 > n3:
            print('Correct!')
if userChoice == n2:
    if n2 > n1:
        if n2 > n3:
            print('Correct!')
if userChoice == n3:
    if n3 > n2:
        if n3 > n1:
            print('Correct!')