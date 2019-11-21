_str = input()
# _str = 'Sandwich'

for i in range(len(_str)):
    print("Index of '{s}': {i}".format(
        s=_str[i],
        i=i
    ))

"""
Index of '_': _
"""