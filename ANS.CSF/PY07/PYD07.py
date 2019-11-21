# _list = [-4, 0, 37, 19, 26, -43, 9]
_list = []
while True:
    n = int(input())
    if n == -9999:
        break
    
    _list.append(n)

_tuple = tuple(_list)
print('Length: {len}'.format(len=len(_tuple)))
print('Max: {max}'.format(max=max(_tuple)))
print('Min: {min}'.format(min=min(_tuple)))
print('Sum: {sum}'.format(sum=sum(_tuple)))


"""
Length: _
Max: _
Min: _
Sum: _
"""