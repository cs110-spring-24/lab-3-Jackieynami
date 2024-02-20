import string


print("option: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
run = input("Enter the problem you want to run: ")
run = int(run)
if run == 1:
    print("Running problem 1")
    for count in range(1, 1001):
        print(count)
    # Your code for problem 1 goes here
elif run == 2:
    print("Running problem 2")
    for count in range(1, 1001, 2 ):
        print(count)
    # Your code for problem 2 goes here
elif run == 3:
    print("Running problem 3")
    for count in range(0, 1001):
        if (count % 3 == 0):
            print(count)
    # Your code for problem 3 goes here
elif run == 4: 
    print("Running problem 4")
    for count in range(1, 1001):
        if (count % 3 == 0 or count % 5 == 0):
            print(count)
    # Your code for problem 4 goes here

# Enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200.
# Extra credit if the programs asks again if the number is less than 200
    
elif run == 5:
    user = int(input("Enter a number greater than 200: "))
    while user < 200:
        print(user, "Is less than 200")
        user = int(input("Enter a number greater than 200: "))
    for count in range(1, user):
        if (count % 11 == 0 or count % 13 == 0):
            print(count)

# Write a program that prints out each letter of a string line by line.
elif run == 6:
    string = input("Enter a word: ")
    for count in range(0, len(string)):
        print(string[count])

# Write a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long.
elif run == 7:
    string == input("Enter a word over 10 letters long: ")
    for count in range(0, len(string), 2):
        print(string[count])

# Write a program that rolls 1000 dice and prints out the number of times each number was rolled.
elif run == 8:
    import random
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0

    for roll in range(1000):
        dice = random.randint(1, 6)
        if dice == 1:
            ones += 1
        elif dice == 2:
            twos += 1
        elif dice == 3:
            threes += 1
        elif dice == 4:
            fours += 1
        elif dice == 5:
            fives += 1
        else:
            sixes += 1
        print(f"You rolled {ones} 1s, {twos} 2s, {threes} 3s, {fours} 4s, {fives} 5s, and {sixes} 6s")

# Write a program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not.
elif run == 9:
    user = int(input("Enter a number: "))
    for prime in range(2, user):
        if (user % prime == 0):
            print(user, "Is not a prime number")
            break
        else:
            print (user, "Is a prime number")


# Write a program that prints out the prime numbers less than 1000.
elif run == 10:
    for count in range (1, 1001):
        if count <=1:
            continue
        elif count == 2:
            print(count)
        else:
            Is_prime = True 
            for prime in range(2, count):
                if count % prime == 0:
                    Is_prime = False
                    break
            if Is_prime == True:
                print(count)












    




