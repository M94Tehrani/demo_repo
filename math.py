def fact(x):
    i, r = 1,1
    while i <= x:
        r = r * i
        i+=1
    return r

result = fact(3)
print(result)


