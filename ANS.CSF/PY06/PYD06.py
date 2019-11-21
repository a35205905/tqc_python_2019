# _list = [56, 45, 43, 22, 3, 1, 39, 20, 93, 18, 44, 83]
_list = []
sum = 0
for i in range(12):
    n = int(input())
    _list.append(n)
    if i % 2 == 0:
        sum += n

for i in range(4):
    print('{:>3}{:>3}{:>3}'.format(
        _list[i*3],
        _list[i*3+1],
        _list[i*3+2]
    ))

print(sum)