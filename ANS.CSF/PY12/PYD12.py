str1 = input()
str2 = input()

# str1 = 'baaac'
# str2 = 'aaabc'

# str1 = 'aaaaabac'
# str2 = 'aaaaaabc'

# str1 = 'baaac'
# str2 = 'aabca'

# str1 = 'ab'
# str2 = 'ab'

# str1 = ''
# str2 = 'ab'

# str1 = 'AAA'
# str2 = 'aAa'

# 將字串1轉為陣列
str1_list = []
for s in str1:
    str1_list.append(s)

# 逐一交換字母
for i in range(len(str1_list)):
    for j in range(len(str1_list)):
        _list = str1_list.copy()
        # 不與自己交換也不與相同字母交換
        if i != j and _list[i] != _list[j]:
            # print(
            #     'before: {str}|'.format(str=''.join(_list)),
            #     'index: {n}*{s}|'.format(n=i, s=_list[i]),
            #     'index: {n}*{s}|'.format(n=j, s=_list[j]),
            # )
            _list[i], _list[j] = _list[j], _list[i]
            # print('after: {str}'.format(str=''.join(_list)))
            # 與字串2相同
            if ''.join(_list) == str2:
                print('True')
                exit()

print('False')