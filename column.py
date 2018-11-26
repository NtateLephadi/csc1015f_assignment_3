n = eval(input("Enter the start number: "))
i = 0
while n + i * 7 < 41:
    print("%2s" % (n + i * 7))
    i = i + 1
