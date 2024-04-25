n = int(input("Enter a number: "))
count = n + 1

for i in range (n+1):
    count = count - 1
    print(" "*count, i*"#")

