# Function - Bot name and bot birth year
def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

# Function - Bot greeting to user by name
def remind_name():
    print("Please remind me your name.")
    user_name = input()
    print(f"What a great name you have {user_name}!")

# Function - Bot guessing user's age
def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder_three = int(input())
    remainder_five = int(input())
    remainder_seven = int(input())
    age = (remainder_three * 70 + remainder_five * 21 + remainder_seven * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

# Function - Bot counting to a given number
def count():
    print("Now I will prove to you that I can count to any number you want.")
    number_to_count = int(input())
    counter = 0
    while counter <= number_to_count:
        print(str(counter) + " !")
        counter += 1

# Function - Bot testing user's programming knowledge
def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    choice_list = [1, 2, 3, 4]
    choice_input = int(input())
    while choice_input != choice_list[1]:
        print("Please, try again.")
        choice_input = int(input())
    if choice_input == choice_list[1]:
        print("Congratulations, have a nice day!")
    print("Completed, have a nice day!")

# Function - Bot ending communication
def end():
    print("Congratulations, have a nice day!")

# Function calls
greet("Jarvis", "2022")
remind_name()
guess_age()
count()
test()
end()