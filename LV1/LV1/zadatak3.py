from statistics import mean

numbers = []

while 1>0:
    
        print("Enter number: ")
        number = input()
        if(number.isdigit()):
              numbers.append(int(number))
        if number == 'Done':
            break
        elif(not number.isdigit()):
            print("You did not enter a number")

numbers.sort()

print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)} \nMean: {mean(numbers)} \nMax: {max(numbers)} \nMin: {min(numbers)}")