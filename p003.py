a= int(input("a:"))
b= int(input("b:"))
result = 0

for i in range(a, b+1):
    if i % 2 == 1:
        print(i, end=" ")
        result += i
print(result)
