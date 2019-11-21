n1 = str(input())
n2 = str(input())
n3 = str(input())
n4 = str(input())
# n1 = 85
# n2 = 4
# n3 = 299
# n4 = 478

#向右靠齊
print('|{:>5} {:>5}|'.format(n1, n2))
print('|{:>5} {:>5}|'.format(n3, n4))

#向左靠齊
print('|{:<5} {:<5}|'.format(n1, n2))
print('|{:<5} {:<5}|'.format(n3, n4))