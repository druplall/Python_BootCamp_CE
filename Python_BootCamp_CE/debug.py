import random

def generateRandom(upper):
    r = random.randint(1,upper)
    return r

def main():
    run = True
    num1 = generateRandom(10)
    num2 = generateRandom(10)
    results = num1 * num2
    while run:
        ans = input("What is " + str(num1) + " x " + str(num2) + "? ")

        if ans.isdigit():
            if int(ans) == results:
                print('Correct!')
                run = False
            else:
                print("Incorrect ! Try again.")
        else:
            print("Answer must be a positive number, try again.")

# Global Vars
# Testing master push
time = 10
for i in range(time):
    main()