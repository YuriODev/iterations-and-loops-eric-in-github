a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

for i in range(a, b + 1):
    if i % c == 0:
        print(i, end=" ")