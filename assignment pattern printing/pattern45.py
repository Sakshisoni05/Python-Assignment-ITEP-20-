#     1
#    12
#   123
#  1234
# 12345

for i in range(1,6):
        for space in range(5,i,-1):
            print(" ",end="")
            
        for j in range(1,i+1):
          print(j,end="")
        
        print()    
        