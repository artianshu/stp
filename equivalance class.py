try:
    n = int(input("Enter the number:"))
    if n >= 1 and n <= 100:
        print("Valid Range")
    else:
        print("Invalid Range")
except Exception as e:
    print("Invalid Input")
    print("Integer input only")
else:
    print("Validation Successful")