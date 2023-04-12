# n1 = int(input('First number: '))
# n2 = int(input('Second number: '))
# n3 = int(input('Third number: '))
# n4 = int(input('Fourth number: '))
# n5 = int(input('Fifth number: '))
# sumOfNumbers = n1 + n2 + n3 + n4 + n5
# print(sumOfNumbers)

# n1 = int(input('First number: '))
# n2 = int(input('Second number: '))
# n3 = int(input('Third number: '))
# n4 = int(input('Fourth number: '))
# n5 = int(input('Fifth number: '))
# n6 = int(input('Sixth number: '))
# averageOfNumbers = (n1 + n2 + n3 + n4 + n5 + n6)/6
# print('Average of numbers you typed: ' + str(round(averageOfNumbers, 2)))

# cat = 'Bob'
# print(cat)
# cat += ' and John'
# print(cat)

# s1 = input('First word: ')
# s2 = input('Second word: ')
# s3 = input('Third word: ')
# s4 = input('Fourth word: ')
# text = s1 + s2 + s3 + s4
# text2 = s1 + ', ' + s2 + ', ' + s3 + ', ' + s4
# text3 = s1 + ' ' + s2 + ' ' + s3 + ' ' + s4
# print(text)
# print(text2)
# print(text3)

# a = int(input('Number: '))
# b = int(input('Number: '))
# c = a < b
# if c:
#     print('C is ' + str(c))
# elif not c:
#     print('C is ' + str(c))

# import time
# c = 1
# print(c)
# time.sleep(1)
# c += 1
# print(c)
# time.sleep(1)
# c += 1
# print(c)
# time.sleep(1)
# c += 1
# print(c)
# time.sleep(1)
# c += 1
# print(c)
# time.sleep(1)

# import time
# userTime = int(input('Give me amount of time: '))
# if userTime < 10:
#     time.sleep(userTime)
# elif userTime >= 10:
#     print("Too long! I no wanna waste' my time")

# import time
# time = time.gmtime()
# print(str(time[3]) + ' ' + str(time[4]) + ' ' + str(time[5]))

# import time
# pcTime = time.gmtime()
# for second in range(60 - pcTime[5]):
#     print(second)
# time.sleep(60 - pcTime[5])
# print('The end')