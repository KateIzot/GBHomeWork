def title_func(word):
    ret = word.title()
    return ret

print(title_func('rgerg'))

word_list = input('enter words (lowercase english)').split()
result =[]
for word in word_list:
    result.append(title_func(word))
print(' '.join(result))