a = int(input("Enter the number you want to check: "))

# variables for generating fibonacci sequence
f3 = 0
f1 = 1
f2 = 1

if a == 0 or a == 1:
    print("Given number is fibonacci number")

else:
    # generating the fibonacci numbers until the generated number is less than  a
    while f3 < a:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == a:
        print("Given number is fibonacci number")
    else:
        print("No it’s not a fibonacci number")