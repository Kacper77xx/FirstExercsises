#Funkcja num i check, 6-11,
print('Give me the first number!')
num = int(input())
print('Give me the second number!')
check = int(input())
if (num)%(check) == 0 and (num)%4 != 0:
    print('Even')
elif (num)%(check) == 0 and (num)%4 == 0:
    print('Even and divisible by 4')
else:
    print('Odd')
