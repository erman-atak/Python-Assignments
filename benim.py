while True:
    number = input("Write a numeric number: ")
    digit = len(number)
    summ = 0

    if number.isdigit():
        for i in range(digit):
            summ += int(number[i]) ** digit #calculates the total number
        if summ == int(number):
            print("Congrats,", number, "is an Armstrong number!")
            break
        else : 
            print(number, "is not an Armstrong number")
            break

    else: print(number, "is not a valid entry")

    import math
    print(dir(math))

