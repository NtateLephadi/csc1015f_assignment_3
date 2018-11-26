n = eval(input("Enter the start number: "))
m = n + 41
for i in range(6):
    for k in range(7):
        print("%2s" % (n + k), end = ' ')
    n = n + 7
    print()