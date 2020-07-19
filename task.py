words = input('Введите любые символы с заглавной или с маленькой буквы: ')
print(len(words))

word1 = lambda x: x.isupper, words
print(list(word1))


# word_upper