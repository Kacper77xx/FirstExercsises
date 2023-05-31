print('Give me a word!')
userWord = str(input())
revWord = userWord[::-1]
# print(revWord)
if revWord == userWord:
    print('Your word is a palindrome')
    print(revWord + ' == ' + userWord)
else:
    print('Your word is not a palindrome')
    print(revWord + ' != ' + userWord)
