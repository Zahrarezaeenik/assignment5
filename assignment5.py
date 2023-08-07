def Checkered_board(m,n):
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0 :
                print("#",end="")
            else:
                print("*",end="")
        print()


n=int(input("Enter n: "))
m=int(input("Enter m: "))
Checkered_board(n,m)