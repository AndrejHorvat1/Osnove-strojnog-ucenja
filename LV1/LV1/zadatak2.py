try:
    print("Imput number between 0.0 and 1.0")
    number=float(input())
    if(number<0.6):
        print("F")
    if(number >=0.6 and number<0.7):
        print("D")
    if(number >=0.7 and number<0.8):
        print("C")
    if(number >=0.8 and number<0.9):
        print("B")
    if(number >=0.9 and number<1.0):
        print("A")
    if(number <0 and number>1.0):
        print("Nuber is not in range between 0,0 and 1.0")

except:
    print("Invalid input")