n1 = int(input())
n2 = int(input())
n3 = int(input())

# n1 = 10
# n2 = 3
# n3 = 5

# n1 = 10
# n2 = 4
# n3 = 6

# n1 = 2
# n2 = 3
# n3 = 5

# n1 = 8
# n2 = 4
# n3 = 2

if n2 > n3:
    n2, n3 = n3, n2

sum = 0
for n in range(n2, n1):
    if n % n2 == 0:
        sum += n
        print(n)
    elif n % n3 == 0:
        sum += n
        print(n)

print(sum)