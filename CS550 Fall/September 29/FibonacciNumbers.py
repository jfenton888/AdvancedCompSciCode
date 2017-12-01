maxNum = int(input("what fibonacci number do you want"))
f = 0
g = 1
for i in range(0, maxNum):
    f = f + g
    g = f - g
print(f)