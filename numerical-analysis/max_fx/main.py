def f(x):
    return 3* (x**3) - 5 * (x**2) # + 7*x - 12

n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))

max = None
for i in range(n+1):
    x = a + (b-a)*i/n
    ret = f(x)
    print(x, ret)
    if max == None or max < ret:
        max = ret

print(max)
