#try except statment 


try:
    print("execution start")
    while True:
        a = int(input("Enter the value: "))
        b = int(input("Enter the value: "))
        if a>b:
            print(a/b)
        else:
            print("Make sure given value is always greater than value of b")

except Exception :
    print("please sure your value always be an integer")