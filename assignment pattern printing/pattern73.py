# * * * * * 
#  * * * * 
#   * * * 
#    * *  
#     *

for i in range(5):
    for space in range(i):
        print(" ", end="")

    for star in range(5-i):
        print("*", end=" ")

    print()