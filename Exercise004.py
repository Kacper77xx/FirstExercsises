print('Give me your name! There is no reason about it ;)')
yourName = input()
if len(yourName) >= 2:
    print('Give me a random text!')
    userWords = input('Paste here, please: ')
    searchWord = input('Word which you looking for: ')
    if userWords.find(searchWord) >= 0:
        print('There is a ' + str(searchWord) + ' in the sentence')
        print("Your word's/words' location is: " + str(userWords.find(searchWord)))
    else:
        print('There is no' + ' ' + str(searchWord) + ' ' + 'in the sentence')
    print('Cheers, ' + str(yourName.capitalize()) + '!')
    while True:
        print('Again? :)')
        again = input('(y/n): ')
        if again.lower() != 'y':
            print('Goodbye!')
            break
        else:
            print('Give me your name! There is no reason about it ;)')
            yourName = input()
            if len(yourName) >= 2:
                print('Give me a random text!')
                userWords = input('Paste here, please: ')
                searchWord = input('Word which you looking for: ')
                if userWords.find(searchWord) >= 0:
                    print('There is a ' + str(searchWord) + ' in the sentence')
                    print("Your word's/words' location is: " + str(userWords.find(searchWord)))
                else:
                    print('There is no' + ' ' + str(searchWord) + ' ' + 'in the sentence')
                    print('Cheers, ' + str(yourName.capitalize()) + '!')
else:
    while True:
        print('There is no name, program could close, but it has not to! Again? :)')
        again = input('(y/n): ')
        if again.lower() != 'y':
            print('Goodbye!')
            break
        else:
            print('Give me your name! There is no reason about it ;)')
            yourName = input()
            if len(yourName) >= 2:
                print('Give me a random text!')
                userWords = input('Paste here, please: ')
                searchWord = input('Word which you looking for: ')
                if userWords.find(searchWord) >= 0:
                    print('There is a ' + str(searchWord) + ' in the sentence')
                    print("Your word's/words' location is: " + str(userWords.find(searchWord)))
                else:
                    print('There is no' + ' ' + str(searchWord) + ' ' + 'in the sentence')
                print('Cheers, ' + str(yourName.capitalize()) + '!')
                while True:
                    print('Again? :)')
                    again = input('(y/n): ')
                    if again.lower() != 'y':
                        print('Goodbye!')
                        break
                    else:
                        print('Give me your name! There is no reason about it ;)')
                        yourName = input()
                        if len(yourName) >= 2:
                            print('Give me a random text!')
                            userWords = input('Paste here, please: ')
                            searchWord = input('Word which you looking for: ')
                            if userWords.find(searchWord) >= 0:
                                print('There is a ' + str(searchWord) + ' in the sentence')
                                print("Your word's/words' location is: " + str(userWords.find(searchWord)))
                            else:
                                print('There is no' + ' ' + str(searchWord) + ' ' + 'in the sentence')
                                print('Cheers, ' + str(yourName.capitalize()) + '!')

