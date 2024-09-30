a = int(input())
result = ""
if a % 2 == 0:
    f = a // 2
else:
    f = (a // 2) + 1
for i in range(1,f):
    for j in range(i+1,a - i + 1):
        if a % (i + j) == 0:
            result += str(i) + str(j)
print(result)


