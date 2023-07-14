import random

response = "y"
while response == "y":
    number = random.randint(1,6)

    if number==1:
        print("0")
    if number==2:
        print("0")    
        print("  0")   
    if number==3:
        print("0")    
        print("  0") 
        print("     0")     
    if number==4:
        print("0  0")    
        print("0  0") 
    if number==5:
        print("0  0")    
        print("  0  ")   
        print("0  0")   
    if number==5:
        print("0 0 0")     
        print("0 0 0")   

    response = input("Press y to continue rolling the dice.")        
              