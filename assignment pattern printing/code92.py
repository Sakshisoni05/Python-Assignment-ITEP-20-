for i in range(7):

    for j in range(7):

        if j == i or j == 6-i:
            print("*", end="")
        else:
            print(" ", end="")

    print()