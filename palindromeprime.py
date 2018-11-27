N = eval(input("Enter the start point N:\n"))
M = eval(input("Enter the end point M:\n"))
      
for i in range(N, M + 1):
    n = str(i)
    if n == n[::-1]:
        prime = True
        for j in range(2, i - 1):
            if i % j == 0:
                prime = False
        if prime:
            print(i)