file = open("write.txt", 'w')
# _list = ['Leon 87', 'Ben 90', 'Sam 77', 'Karen 92', 'Kelena 92']
_list = []
for _ in range(5):
    _list.append(input())

file.write('\n'.join(_list))
file.close()