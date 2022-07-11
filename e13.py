num = []
n = 1

for n in range(1,11):
    n = int(input('digite n: '))
    if n!=0 : num.append(n)
print(num)
print(num[::-1])